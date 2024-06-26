# Gene-Amplification-and-SNP-Analysis
Final project
# Gene Amplification and SNP Analysis using VCF Files

## Project Overview
This project explores the role of double-strand breaks (DSBs) in the formation of gene amplifications and analyzes Single Nucleotide Polymorphisms (SNPs) from VCF files. The program generates an Excel file with SNP locations, and the user can choose is own DNA location and look for SNP  positions..

## Scientific Background
- **Gene Amplification**: A hallmark in cancer contributing to tumorigenesis, intra-tumor heterogeneity, and drug resistance.
- **Double-Strand Breaks (DSBs)**: Critical DNA lesions involved in genomic instability.
- **SNPs**: Variations at single nucleotide positions, significant in genetic research and disease association.

## Single Nucleotide Polymorphisms (SNPs)
SNPs are variations at a single nucleotide position in the genome, and they can be associated with various diseases, including cancer. Identifying SNP locations can help in understanding genetic variations and their implications in disease mechanisms.
VCF File Format: A standard format for storing genetic variations. VCF files contain information about SNPs, insertions, deletions, and other variants.


## Technical Implementation
1. Clone the repository:
    ```bash
    git clone https://github.com/AdiBarelMeisel/Gene-Amplification-and-SNP-Analysis/blob/main/README.md
    cd Gene-Amplification-and-SNP-Analysis

    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Running the Program
   The program processes VCF files and outputs an Excel file with SNP locations.
4. Graphical User Interface 
  Open a window to input parameters using GUI.
  Input Data

To run the program with a VCF file:
```bash
python project.py input.vcf

5. Testing
 Run tests using pytest to ensure the program works correctly.

bash
Copy code
pytest

