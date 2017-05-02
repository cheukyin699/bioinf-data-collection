# Meaning of the Various Filenames

## General Format

To be processed correctly, the filenames should be named like this:

```
<specimen>_<cropped?>_<grouping>.<extension>
```

**Where:**

- `<specimen>` is the specimen (i.e. E. Coli)
- `<cropped?>` is either `N30` or `WHOLE` meaning the first 30 proteins
  (cropped) or the entire genome
- `<grouping>` is the group that the data is in (Pos, Neg, Test), either the
  positive group, negative, or test group. Pos and Neg are part of the training
  data, and Test is the stuff you don't know yet
- `<extension>` is the file extension `pepinfo`, `pepprop`, `protout`, `cai`,
  `poodle`, or `gpc`

## Various Attributes

Attribute | Extension | N30/WHOLE
----------|-----------|----------
Tiny      | pepprop   | N30
Small     | pepprop   | N30
Aliphatic | pepprop   | N30
Aromatic  | pepprop   | N30
Polar     | pepprop   | N30
Non-Polar | pepprop   | N30
Charged   | pepprop   | N30
Basic     | pepprop   | N30
Acidic    | pepprop   | N30
Molecular Weight | pepinfo | Whole
Charge    | pepinfo   | N30
A280 Molar Extinction Coefficients  | pepinfo | N30
A280 Extinction Coefficients 1mg/ml | pepinfo | N30
Probability of expression in inclusion bodies | pepinfo | N30
Isoelectric Point(Theoretical pI)   | protout | N30
Codon Adaption index | cai     | Whole
Instability Index    | protout | Whole
Aliphatic index      | protout | N30
GRAVY score          | protout | N30
N-Terminal disorder  | poodle  | N30
G+C content          | gpc     | Whole

## Content in Various Types of Input Files

### PEPPROP (*.pepprop)

Delimited by numerous spaces.

Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 | Col 9 | Col 10
---|---|---|---|---|---|---|---|---|---
Protein Name | Tiny Property Mole% | Small Property Mole% | Aliphatic Property Mole% | Aromatic Property Mole% | Non-Polar Mole% | Polar Mole% | Charged Mole% | Basic Mole% | Acidic Mole%

### PEPINFO (*.pepinfo)

Delimited by numerous spaces.

Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8
---|---|---|---|---|---|---|---
Protein Name | Molecular Weight | Average Residue Weight | Isoelectric Point | Charge | A280 Molar Extinction Coefficients | A280 Extinction Coefficients | Improbability of Expression in Inclusion Bodies

### PROTOUT (*.protout)

Delimited by a tab. Each entry on the table is spaced out with a new-line.

Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7
---|---|---|---|---|---|---
Protein Name | Molecular Weight | Charge | Theoretical pI | Instability Index | Aliphatic Index | Hydropathicity

### CAI (*.cai)

Delimited by 4 spaces. Very neat.

Col 1 | Col 2
---|---
Protein Name | Codon Adaption Index

### POODLE (*.poodle)

Delimited by tabs. For the filename, note:

> Everything but `<cropped?>` is in lower case.

Col 1 | Col 2 | Col 3
---|---|---
Protein Name | Whole Average | N-Terminal Disorder (highly likely)

### GPC (*.gpc)

Delimited by tabs.

Col 1 | Col 2
---|---
Protein Name | G+C Content

## Content in Various Types of Output Files

Both output files are in CSV format with the following columns:

Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 | Col 9 | Col 10 | Col 11 | Col 12 | Col 13 | Col 14 | Col 15 | Col 16 | Col 17 | Col 18 | Col 19 | Col 20 | Col 21 | Col 22 | Col 23
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
Protein Name | Tiny | Small | Aliphatic | Aromatic | Non-Polar | Polar | Charged | Basic | Acidic | Isoelectric Point | Charge | A280 Molar Coefficients | A280 Extinction Coefficients 1mg/mL | Probability of Expression in Inclusion Bodies | Instability Index | Aliphatic Index | GRAVY | CAI | GPC Content | Molecular Weight | N-30 Disorder | Polarity
