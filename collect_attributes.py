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
