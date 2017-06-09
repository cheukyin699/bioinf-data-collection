# Data Collection Script for WEKA

Title is slightly misleading. It converts raw nucleotide data (positives,
negatives, and tests) into a single CSV file, ready to be edited slightly into a
functioning WEKA file.

## Usage

```sh
./collect_attributes.py <FOLDER NAME> <SPECIMEN NAME> [-a|--all] [-o|--output] <DIRECTORY>
```

**FOLDER NAME**: Name of folder where all the files are (i.e. `DATA/`). **Note**:
Must contain the `/` (or `\` if on Windows) at the end.

**SPECIMEN NAME**: Name of the specimen (i.e. `Ecoli`). Capitalization is
optional.

**DIRECTORY**: Name of the output directory for all the output files. Must
contain the `/` or `\` at the end.

Outputs 2 files: 1 file of training data and another for testing. Both files are
in comma-separated value format. The output data will be named
`<SPECIMEN NAME>_Training.csv` and `<SPECIMEN NAME>_Testing.csv`. They will be
written to the current directory, or `<DIRECTORY>` if that option is specified.


## Example Directory Setup

Files necessary for the test/training sets (using organism E. Coli as an
example):

```
Ecoli_N30_neg.pepinfo
Ecoli_N30_neg.pepprop
Ecoli_N30_neg.poodle
Ecoli_N30_neg.protout
Ecoli_N30_pos.pepinfo
Ecoli_N30_pos.pepprop
Ecoli_N30_pos.poodle
Ecoli_N30_pos.protout
Ecoli_N30_test.pepinfo
Ecoli_N30_test.pepprop
Ecoli_N30_test.poodle
Ecoli_N30_test.protout
Ecoli_Nuc_neg.cai
Ecoli_Nuc_neg.gpc
Ecoli_Nuc_pos.cai
Ecoli_Nuc_pos.gpc
Ecoli_Nuc_test.cai
Ecoli_Nuc_test.gpc
Ecoli_WHOLE_neg.protout
Ecoli_WHOLE_pos.protout
Ecoli_WHOLE_test.protout
```

Files necessary for the entire set (happens when `-a` or `--all` is used), using
organism S. Fredii as an example):

```
Sfredii_N30_all.pepinfo
Sfredii_N30_all.pepprop
Sfredii_N30_all.poodle
Sfredii_N30_all.protout
Sfredii_Nuc_all.cai
Sfredii_Nuc_all.gpc
Sfredii_WHOLE_all.pepinfo
Sfredii_WHOLE_all.pepprop
Sfredii_WHOLE_all.protout
```
