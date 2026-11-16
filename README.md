# DNA Sequence Analysis Tool

## About the Project

DNA Sequence Analysis Tool is a beginner-level bioinformatics project developed using Python.

It is an interactive command-line application that performs fundamental DNA sequence analysis operations. The program accepts a DNA sequence, validates it, and allows users to perform different analyses through a menu-driven interface.

This project demonstrates the application of Python programming concepts to basic molecular biology and bioinformatics.

## Features

1. **DNA Sequence Validation:** Checks whether the input contains only valid DNA nucleotides (A, T, G and C).
2. **Sequence Length:** Calculates the total number of nucleotides in the DNA sequence.
3. **Nucleotide Frequency:** Calculates the frequency of A, T, G and C.
4. **GC Content:** Calculates the percentage of guanine (G) and cytosine (C) in the DNA sequence.
5. **Coding Strand Transcription:** Converts a coding DNA strand (5' to 3') into mRNA by replacing T with U.
6. **Template Strand Transcription:** Converts a template DNA strand (3' to 5') into its complementary mRNA sequence.

## Technologies Used

- Python 3
- String Manipulation
- Functions
- Loops and Conditional Statements
- Exception Handling

## How to Run

1. Clone or download this repository.
2. Ensure Python 3 is installed.
3. Open a terminal in the project directory.
4. Run:

```bash
python dna_analysis.py
```

5. Enter a valid DNA sequence.
6. Select the desired analysis from the menu.

## Example

**Input DNA sequence:**

```text
ATGC
```

**Sequence Length:**

```text
4
```

**Nucleotide Frequency:**

```text
A: 1
T: 1
G: 1
C: 1
```

**GC Content:**

```text
50.00%
```

**Coding Strand Transcription:**

```text
AUGC
```

**Template Strand Input (3' to 5'):**

```text
TACG
```

**Template Strand Transcription:**

```text
AUGC
```

## Learning Outcomes

- Understanding DNA sequence validation.
- Working with biological sequence data.
- Implementing nucleotide frequency calculations.
- Calculating GC content.
- Applying Python functions and string manipulation to bioinformatics.

## Future Improvements

- Support FASTA file input.
- Save analysis results to output files.
- Introduce graphical data visualization.

## Author

Mukund Kulkarni

MSc Bioinformatics Student
