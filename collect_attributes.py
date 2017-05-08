#!/usr/bin/env python3
import argparse as ag
import sys
from collections import defaultdict

# Argument parsing (just don't a bunch of if statements and get screwed over,
# m'kay?)
parser = ag.ArgumentParser(
description='''turns a bunch of attribute data into
WEKA-compatible CSV training and testing data.''',
epilog='''outputs 2 files - 1 for training and 1 for testing.''')
parser.add_argument('folder', metavar='<folder>', type=str,
                    help='name of folder where all the data files are. Must end with slash')
parser.add_argument('specimen', metavar='<specimen>', type=str,
                    help='name of specimen (i.e. Ecoli). Capitalization is optional')
parser.add_argument('-o', '--output', type=str, metavar='dir', default='./',
                    help='directory of output files (default: current directory)')
# Arguments stored with attributes .folder, .specimen, and .directory
# Everything is stored correctly because that's how argparse works.
args = parser.parse_args()

# Output filenames
training_filename = args.output + '%s_Training.csv' % args.specimen
testing_filename = args.output + '%s_Testing.csv' % args.specimen

# Input filename (template)
template = args.folder + '%s_%s_%s.%s'

# Total number of attributes (not counting Polarity)
NUM_ATTRIBUTES = 21
# What to say if the protein reads positive
POSITIVE = 'TRUE'
# What to say if the protein reads negative
NEGATIVE = 'FALSE'
# What to say if the protein reads negative
TEST = '?'
# CSV file header
CSV_HEADER = ','.join([
        'Protein Name',
        'Tiny',
        'Small',
        'Aliphatic',
        'Aromatic',
        'Non-Polar',
        'Polar',
        'Charged',
        'Basic',
        'Acidic',
        'Molecular Weight',
        'Charge',
        'A280 Molar Extinction Coefficients',
        'A280 Extinction Coefficients 1mg/mL',
        'Improbability of expression in inclusion bodies',
        'Isoelectric Point',
        'CAI',
        'Instability Index',
        'Aliphatic Index',
        'GRAVY',
        'N-30 Disorder',
        'GPC Content',
        'Effector'
        ])


def make_type_templates(t):
    '''
    Creates a list of fill-ins for template `template` with type t.

    Parameters:
    t - the template type; either 'pos', 'neg', or 'test'

    Returns:
    A list of fill-ins for the template for input filenames.
    '''
    s = t.lower()
    s_c = args.specimen.capitalize()
    return [(s_c, 'N30',   s, 'pepprop'),
            (s_c, 'N30',   s, 'pepinfo'),
            (s_c, 'N30',   s, 'protout'),
            (s_c, 'WHOLE', s, 'protout'),
            (s_c, 'Nuc',   s, 'cai'),
            (s_c, 'N30',   s, 'poodle'),
            (s_c, 'Nuc',   s, 'gpc')]

def parse_pepprop(d, line):
    '''
    Parses the line that is (supposed) in .pepprop format (with formatting and
    column names).

    Parameters:
    d       - the dictionary to add the entries to
    line    - the line in pepprop format (4 spaces 10 columns)

    Returns:
    Nothing. Just updates the dictionary.
    '''
    cols = line.split()

    for i in range(9):
        d[cols[0]][i] = cols[i+1]

def parse_pepinfo(d, line, t):
    '''
    Parses the line that is (supposed) in .pepinfo format (with formatting and
    column names).

    Parameters:
    d       - the dictionary to add the entries to
    line    - the line in pepprop format (4 spaces 8 columns)
    t       - the type of the file (N30/WHOLE)

    Returns:
    Nothing. Just updates the dictionary.
    '''
    cols = line.split()

    if t == 'N30':
        # Charge
        d[cols[0]][10] = cols[4]
        # A280 Molar Extinction Coefficient
        d[cols[0]][11] = cols[5]
        # A280 Extinction Coefficients
        d[cols[0]][12] = cols[6]
        # Probability of Expression in Inclusion Bodies
        # Per the docs, this is actually the IMprobability, but I guess they
        # both are similar enough
        d[cols[0]][13] = cols[7]
    #elif t == 'WHOLE':
        # Molecular Weight
        #d[cols[0]][9] = cols[1]
    else:
        raise RuntimeError('error: invalid argument %s' % t)

def parse_protout(d, line, t):
    '''
    Parses the line that is (supposed) in .protout format (with formatting and
    column names).

    Parameters:
    d       - the dictionary to add the entries to
    line    - the line in protout format (1 tab 7 columns)
    t       - the type of the file (N30/WHOLE)

    Returns:
    Nothing. Just updates the dictionary.
    '''
    cols = line.split()

    if t == 'N30':
        # Instability Index
        d[cols[0]][16] = cols[4]
        # Aliphatic Index
        d[cols[0]][17] = cols[5]
        # GRAVY score
        # (Grand Average of hydropathy)
        d[cols[0]][18] = cols[6]
    elif t == 'WHOLE':
        # Isoelectric Point
        d[cols[0]][14] = cols[3]
        # Molecular Weight
        d[cols[0]][9] = cols[1]
    else:
        raise RuntimeError('error: invalid argument %s' % t)

def parse_cai(d, line):
    '''
    Parses the line that is (supposed) in .cai format (with formatting and
    column names).

    Parameters:
    d       - the dictionary to add the entries to
    line    - the line in cai format (4 spaces 2 columns)

    Returns:
    Nothing. Just updates the dictionary.
    '''
    cols = line.split()

    d[cols[0]][15] = cols[1]

def parse_poodle(d, line):
    '''
    Parses the line that is (supposed) in .poodle format (with formatting and
    column names).

    Parameters:
    d       - the dictionary to add the entries to
    line    - the line in cai format (1 tab 3 columns)

    Returns:
    Nothing. Just updates the dictionary.
    '''
    cols = line.split()

    d[cols[0]][19] = cols[2]

def parse_gpc(d, line):
    '''
    Parses the line that is (supposed) in .gpc format (with formatting and
    column names).

    Parameters:
    d       - the dictionary to add the entries to
    line    - the line in cai format (1 tab 2 columns)

    Returns:
    Nothing. Just updates the dictionary.
    '''
    cols = line.split()

    d[cols[0]][20] = cols[1]


pos_templ = make_type_templates('pos')
negs_templ = make_type_templates('neg')
tests_templ = make_type_templates('test')

# Every entry is a list with size 22 - 1 for each attribute, as specified per
# the documentation. For info on the order, see `docs/filename_meanings.md`
# In vim, put your cursor at the start of the filename, and press <C-W>gf.
def defaults():
    return list(range(NUM_ATTRIBUTES))

positives = defaultdict(defaults)
negatives = defaultdict(defaults)
tests = defaultdict(defaults)

# This is for less repetition
templ_dict_pairs = [
        (pos_templ, positives),
        (negs_templ, negatives),
        (tests_templ, tests)]

# Go through the pair of templates-dictionaries, adding to them accordingly
for ts, d in templ_dict_pairs:
    for t in ts:
        try:
            infile = open(template % t, 'r')

            for l in infile.readlines():
                l = l.rstrip()
                if l in '': continue

                if t[3] == 'pepprop':
                    parse_pepprop(d, l)
                elif t[3] == 'pepinfo':
                    parse_pepinfo(d, l, t[1])
                elif t[3] == 'protout':
                    parse_protout(d, l, t[1])
                elif t[3] == 'cai':
                    parse_cai(d, l)
                elif t[3] == 'poodle':
                    parse_poodle(d, l)
                elif t[3] == 'gpc':
                    parse_gpc(d, l)

            infile.close()
        except IOError:
            print('error: unable to find file `%s\'' % (template % t))

# Go through the positives and negatives, putting them into a larger, sorted
# array. Sorts by protein name
# Also goes through testing data, putting them into a sorted array
combined_training = []
combined_testing = []
for name, attrs in positives.items():
    combined_training.append(list(range(NUM_ATTRIBUTES+2)))
    for i in range(NUM_ATTRIBUTES):
        combined_training[-1][i+1] = attrs[i]
    combined_training[-1][-1] = POSITIVE
    combined_training[-1][0] = name
for name, attrs in negatives.items():
    combined_training.append(list(range(NUM_ATTRIBUTES+2)))
    for i in range(NUM_ATTRIBUTES):
        combined_training[-1][i+1] = attrs[i]
    combined_training[-1][-1] = NEGATIVE
    combined_training[-1][0] = name
for name, attrs in tests.items():
    combined_testing.append(list(range(NUM_ATTRIBUTES+2)))
    for i in range(NUM_ATTRIBUTES):
        combined_testing[-1][i+1] = attrs[i]
    combined_testing[-1][-1] = TEST
    combined_testing[-1][0] = name
combined_training.sort(key=lambda i: i[0])
combined_testing.sort(key=lambda i: i[0])

# Write everything to CSV file
try:
    train_file = open(training_filename, 'w')
    test_file = open(testing_filename, 'w')

    # Write the headers to both
    train_file.write(CSV_HEADER + '\n')
    test_file.write(CSV_HEADER + '\n')

    # Write all the data to both
    for item in combined_training:
        train_file.write(','.join(item) + '\n')
    for item in combined_testing:
        test_file.write(','.join(item) + '\n')

    train_file.close()
    test_file.close()
except IOError:
    print('error: unable to write to files `%s\' and/or `%s\'' %
            (training_filename, testing_filename))
