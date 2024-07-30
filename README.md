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

1. Requirements

    - Python 3.x
    - pandas
    - pytest

    To install the required packages, use the following command:

    ```sh
    pip install -r requirements.txt
    ```

2. Running the Program:
    The vcf_parser.py script provides several subcommands to parse SNPs from VCF files. The general syntax is:

    ```sh
    python vcf_parser.py <command> [options]
    ```
    Commands
    - **all**: Parse all SNPs in the VCF file into a CSV file.

        ```sh
        python vcf_parser.py all <vcf_file> <output_csv>
        ```

        **<vcf_file>**: Path to the input VCF file.
        **<output_csv>**: Path to the output CSV file.

        *Example:*
        ```sh
        python vcf_parser.py all vcif_snippet.vcf output_all_snps.csv
        ```
        
    - **chromosome**: Parse SNPs from a specific chromosome into a CSV file.
         ```sh
        python vcf_parser.py chromosome <vcf_file> <chromosome> <output_csv>
        ```
        **<vcf_file>**: Path to the input VCF file.
        **<chromosome>**: Chromosome to filter SNPs (e.g., 1, 2, ..., X, Y).
        **<output_csv>**: Path to the output CSV file.

        *Example:*
        ```sh
        python vcf_parser.py chromosome vcif_snippet.vcf 1 output_chromosome_snps.csv
        ```

    - **chromosome_nucleotide**: Parse SNPs from a specific chromosome and nucleotide into a CSV file.
        ```sh
        python vcf_parser.py chromosome_nucleotide <vcf_file> <chromosome> <nucleotide> <output_csv>
        ```
        **<vcf_file>**: Path to the input VCF file.
        **<chromosome>**: Chromosome to filter SNPs (e.g., 1, 2, ..., X, Y).
        **<nucleotide>**: Nucleotide to filter SNPs (e.g., A, G, T, C).
        **<output_csv>**: Path to the output CSV file.
        
        *Example:*

        ```sh
        python vcf_parser.py chromosome_nucleotide vcif_snippet.vcf 1 G output_chromosome_nucleotide_snps.csv
        ```

    - **significant**: Parse significant SNPs (P-value < 0.05) from a specific chromosome into a CSV file.

        ```sh
        python vcf_parser.py significant <vcf_file> <chromosome> <nucleotide> <output_csv>
        ```
        **<vcf_file>**: Path to the input VCF file.
        **<chromosome>**: Chromosome to filter significant SNPs (e.g., 1, 2, ..., X, Y).
        **<nucleotide>**: Nucleotide to filter SNPs (e.g., A, G, T, C).
        **<output_csv>**: Path to the output CSV file.

        *Example:*
        ```sh
        python vcf_parser.py significant vcif_snippet.vcf 1 G output_significant_snps.csv
        ```

3. Testing
 Run tests using pytest to ensure the program works correctly.

    ```sh
    pytest test_vcf_parser.py
    ```

> This project was originally implemented as part of the [Python programming course](https://github.com/szabgab/wis-python-course-2024-04)
> at the [Weizmann Institute of Science](https://www.weizmann.ac.il/) taught by [Gabor Szabo](https://szabgab.com/)
