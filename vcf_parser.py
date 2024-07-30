import pandas as pd
import argparse
import os

# function to convert a vcf file to a pandas dataframe
def vcf_to_dataframe(vcf_file_path):
    data = []
    header = []

    with open(vcf_file_path, 'r') as vcf:
        for line in vcf:
            if not line.startswith('##'):
                # If the line starts with '#', it's the header
                if line.startswith('#'):
                    header = line.lstrip('#').strip().split('\t')
                else:
                    data.append(line.strip().split('\t'))

    # Create a DataFrame using the collected data and header
    df = pd.DataFrame(data, columns=header)
    return df


def validate_inputs(vcf_file, chromosome=None, nucleotide=None):
    valid_chromosomes = [str(i) for i in range(1, 24)] + ['x', 'y']
    valid_nucleotides = ['A', 'G', 'T', 'C']

    # Check if VCF file can be read
    if not os.path.isfile(vcf_file) or not vcf_file.endswith('.vcf'):
        raise ValueError("The VCF file is not valid or cannot be read.")

    # Check chromosome validity
    if chromosome and chromosome.lower() not in valid_chromosomes:
        raise ValueError("Chromosome must be between 1-23, or 'x' or 'y'.")

    # Check nucleotide validity
    if nucleotide and nucleotide.upper() not in valid_nucleotides:
        raise ValueError("Nucleotide must be one of A, G, T, C.")


def parse_all_snps(vcf_file, output_csv):
    vcf_to_dataframe(vcf_file).to_csv(output_csv)


def parse_snps_by_chromosome(vcf_file, chromosome):
    df = vcf_to_dataframe(vcf_file)
    df = df.drop(["TUMOUR", "FORMAT", "INFO", "FILTER", "QUAL"], axis=1)
    df = df.loc[df['CHROM'] == chromosome]
    return df


def parse_snps_by_chromosome_and_nucleotide(vcf_file, chromosome, nucleotide):
    df = parse_snps_by_chromosome(vcf_file, chromosome)
    df = df.loc[(df['REF'] == nucleotide) | (df['ALT'] == nucleotide)]
    return df


def parse_significant_snps(vcf_file, chromosome, nucleotide):
    df = parse_snps_by_chromosome_and_nucleotide(vcf_file, chromosome, nucleotide)
    split_NORMAL_column = df['NORMAL'].str.split(':', expand=True)

    # Assign new column names
    split_NORMAL_column.columns = ["NORMAL_TYPE", "NORMAL_A1", "NORMAL_C1", "NORMAL_G1", "NORMAL_T1", "NORMAL_A2",
                                   "NORMAL_C2", "NORMAL_G2", "NORMAL_T2", "NORMAL_PVAL"]

    # Concatenate the original DataFrame with the new split columns
    df = pd.concat([df, split_NORMAL_column], axis=1)
    df['NORMAL_PVAL'] = df['NORMAL_PVAL'].apply(lambda x: float(x))
    df = df.loc[df['NORMAL_PVAL'] < 0.05]
    return df


def main():
    parser = argparse.ArgumentParser(description="Analyze SNPs from VCF files.")

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Sub-parser for the 'all' command
    parser_all = subparsers.add_parser('all', help='Parse all SNPs in the VCF file into a CSV file')
    parser_all.add_argument('vcf_file', help='Path to the input VCF file')
    parser_all.add_argument('output_csv', help='Path to the output CSV file')

    # Sub-parser for the 'chromosome' command
    parser_chromosome = subparsers.add_parser('chromosome',
                                              help='Parse SNPs from a specific chromosome into a CSV file')
    parser_chromosome.add_argument('vcf_file', help='Path to the input VCF file')
    parser_chromosome.add_argument('chromosome', help='Chromosome to filter SNPs')
    parser_chromosome.add_argument('output_csv', help='Path to the output CSV file')

    # Sub-parser for the 'chromosome_nucleotide' command
    parser_chromosome_nucleotide = subparsers.add_parser('chromosome_nucleotide',
                                                         help='Parse SNPs from a specific chromosome and nucleotide into a CSV file')
    parser_chromosome_nucleotide.add_argument('vcf_file', help='Path to the input VCF file')
    parser_chromosome_nucleotide.add_argument('chromosome', help='Chromosome to filter SNPs')
    parser_chromosome_nucleotide.add_argument('nucleotide', help='Nucleotide to filter SNPs')
    parser_chromosome_nucleotide.add_argument('output_csv', help='Path to the output CSV file')

    # Sub-parser for the 'significant' command
    parser_significant = subparsers.add_parser('significant',
                                               help='Parse significant SNPs from a specific chromosome into a CSV file')
    parser_significant.add_argument('vcf_file', help='Path to the input VCF file')
    parser_significant.add_argument('chromosome', help='Chromosome to filter significant SNPs')
    parser_significant.add_argument('nucleotide', help='Nucleotide to filter SNPs')
    parser_significant.add_argument('output_csv', help='Path to the output CSV file')

    args = parser.parse_args()

    if args.command == 'all':
        validate_inputs(args.vcf_file)
        parse_all_snps(args.vcf_file, args.output_csv)
    elif args.command == 'chromosome':
        validate_inputs(args.vcf_file, args.chromosome)
        parse_snps_by_chromosome(args.vcf_file, args.chromosome).to_csv(args.output_csv)
    elif args.command == 'chromosome_nucleotide':
        validate_inputs(args.vcf_file, args.chromosome, args.nucleotide)
        parse_snps_by_chromosome_and_nucleotide(args.vcf_file, args.chromosome, args.nucleotide).to_csv(args.output_csv)
    elif args.command == 'significant':
        validate_inputs(args.vcf_file, args.chromosome, args.nucleotide)
        parse_significant_snps(args.vcf_file, args.chromosome, args.nucleotide).to_csv(args.output_csv)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
