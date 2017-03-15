# Data Collection Script for WEKA

Title is slightly misleading. It converts raw nucleotide data (positives,
negatives, and tests) into a single CSV file, ready to be edited slightly into a
functioning WEKA file.

## Usage

```sh
./collect_attributes.py <FOLDER NAME> <SPECIMEN NAME> [-d|--directory] <DIRECTORY>
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
written to the current directory, or `<DIRECTOR>` if that option is specified.
