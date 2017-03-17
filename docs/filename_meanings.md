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

---
Col 1: Protein Name
Col 2: Tiny Property Mole%
Col 3: Small Property Mole%
Col 4: Aliphatic Property Mole%
Col 5: Aromatic Property Mole%
Col 6: Non-Polar Mole%
Col 7: Polar Mole%
Col 8: Charged Mole%
Col 9: Basic Mole%
Col 10: Acidic Mole%
---

### PEPINFO (*.pepinfo)

Delimited by numerous spaces.

---
Col 1: Protein Name
Col 2: Molecular Weight
Col 3: Average Residue Weight
Col 4: Isoelectric Point
Col 5: Charge
Col 6: A280 Molar Extinction Coefficients
Col 7: A280 Extinction Coefficients
Col 8: Improbability of Expression in Inclusion Bodies
---

### PROTOUT (*.protout)

Delimited by a tab. Each entry on the table is spaced out with a new-line.

---
Col 1: Protein Name
Col 2: Molecular Weight
Col 3: Theoretical pI
Col 4: A280 Extinction Coefficients 1mg/mL
Col 5: Instability Index
Col 6: Aliphatic Index
Col 7: GRAVY
---

### CAI (*.cai)

Delimited by 4 spaces. Very neat.

---
Col 1: Protein Name
Col 2: Codon Adaption Index
---

### POODLE (*.poodle)

Delimited by tabs. For the filename, note:

> Everything but `<cropped?>` is in lower case.

---
Col 1: Protein Name
Col 2: IDK LOL
Col 3: ????
---

### GPC (*.gpc)

Delimited by tabs.

---
Col 1: Protein Name
Col 2: G+C Content
---

## Content in Various Types of Output Files

Both output files are in CSV format with the following columns:

---
Col 1: Protein Name
Col 2: Tiny
Col 3: Small
Col 4: Aliphatic
Col 5: Aromatic
Col 6: Non-Polar
Col 7: Polar
Col 8: Charged
Col 9: Basic
Col 10: Acidic
Col 11: Isoelectric Point
Col 12: Charge
Col 13: A280 Molar Coefficients
Col 14: A280 Extinction Coefficients 1mg/mL
Col 15: Probability of Expression in Inclusion Bodies
Col 16: Instability Index
Col 17: Aliphatic Index
Col 18: GRAVY
Col 19: CAI
Col 20: GPC Content
Col 21: Molecular Weight
Col 22: N-30 Disorder
Col 23: Polarity
---

