# Gene Amplification and SNP Analysis using VCF Files

## Project Overview
This project explores the role of double-strand breaks (DSBs) in the formation of gene amplifications and analyzes Single Nucleotide Polymorphisms (SNPs) from VCF files. The program parses VCF files and has four modes:
- Parsing all SNPs in the VCF file into a CSV file
- Parsing SNPs only from a user-chosen chromosome into a CSV file
- Parsing SNPs only from a user-chosen chromosome and a specific nucleotide into a CSV file
- Parsing only the most signifcant SNPs from a user-chosen chromosome into a CSV file

## Scientific Background
- **Gene Amplification**: A hallmark in cancer contributing to tumorigenesis, intra-tumor heterogeneity, and drug resistance.
- **Double-Strand Breaks (DSBs)**: Critical DNA lesions involved in genomic instability.
- **SNPs**: Variations at single nucleotide positions, significant in genetic research and disease association.

## Single Nucleotide Polymorphisms (SNPs)
SNPs are variations at a single nucleotide position in the genome, and they can be associated with various diseases, including cancer. Identifying SNP locations can help in understanding genetic variations and their implications in disease mechanisms.
VCF File Format: A standard format for storing genetic variations. VCF files contain information about SNPs, insertions, deletions, and other variants.


## Technical Implementation

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Running the Program:
    To run the program with a VCF file:
    ```bash
    python project.py path_to_vcf_file.vcf
    ```
    Next the program will ask which mode to run in of the four above ```all/chr/chr_ncltd/chr_signif```,
    and for the latter three, the user will be requested to input the desired chromosme and then the desired nucleotide if required.

3. Testing
 Run tests using pytest to ensure the program works correctly.

```bash
pytest
```

> This project was originally implemented as part of the [Python programming course](https://github.com/szabgab/wis-python-course-2024-04)
> at the [Weizmann Institute of Science](https://www.weizmann.ac.il/) taught by [Gabor Szabo](https://szabgab.com/)
