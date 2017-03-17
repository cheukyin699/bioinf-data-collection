#!/usr/bin/env python3
import argparse as ag
import sys

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
parser.add_argument('-d', '--directory', type=str, metavar='dir', default='./',
                    help='directory of output files (default: current directory)')
# Arguments stored with attributes .folder, .specimen, and .directory
# Everything is stored correctly because that's how argparse works.
args = parser.parse_args()

# Output filenames
training_filename = '%s_Training.csv' % args.specimen
testing_filename = '%s_Testing.csv' % args.specimen

# Input filename (template)
template = '%s_%s_%s.%s'

def make_type_templates(t):
    '''
    Creates a list of fill-ins for template `template` with type t.

    Parameters:
    t - the template type; either 'pos', 'neg', or 'test'

    Returns:
    A list of fill-ins for the template for input filenames.
    '''
    s = t.lower()
    c = t.capitalize()
    s_l = args.specimen.lower()
    return [(args.specimen, 'N30',     c, 'pepprop'),
            (args.specimen, 'N30',     c, 'pepinfo'),
            (args.specimen, 'N30',     c, 'protout'),
            (          s_l, 'WHOLE',   s, 'protout'),
            (args.specimen, 'Nuc',     c, 'cai'),
            (          s_l, 'N30',     s, 'poodle'),
            (args.specimen, 'Nuc',     c, 'gpc')]

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

    try:
        d[cols[0]][:9] = cols[1:]
    except:
        d[cols[0]] = cols[1:] + [None] * 13

def parse_pepinfo(d, line):
    '''
    Parses the line that is (supposed) in .pepinfo format (with formatting and
    column names).

    Parameters:
    d       - the dictionary to add the entries to
    line    - the line in pepprop format (4 spaces 10 columns)

    Returns:
    Nothing. Just updates the dictionary.
    '''
    cols = line.split()

    try:
        d[cols[0]][:9] = cols[1:]
    except:
        d[cols[0]] = cols[1:] + [None] * 13

pos_templ = make_type_templates('pos')
negs_templ = make_type_templates('neg')
tests_templ = make_type_templates('test')

# Every entry is a list with size 22 - 1 for each attribute, as specified per
# the documentation. For info on the order, see `docs/filename_meanings.md`
# In vim, put your cursor at the start of the filename, and press <C-W>gf.
positives = {}
negatives = {}
tests = {}

for p in pos_templ:
    try:
        infile = open(template % p, 'r')

        infile.close()
    except:
        print('error: unable to find file `%s\'' % (template % p))

for n in negs_templ:
    pass

for t in tests_templ:
    pass


