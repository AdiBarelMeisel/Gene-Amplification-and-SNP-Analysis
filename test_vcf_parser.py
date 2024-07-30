from tempfile import NamedTemporaryFile

import pytest
import pandas as pd
import os
from vcf_parser import (
    vcf_to_dataframe, validate_inputs, parse_all_snps,
    parse_snps_by_chromosome, parse_snps_by_chromosome_and_nucleotide,
    parse_significant_snps
)

# Path to the VCF file snippet for testing
VCF_FILE_PATH = 'vcif_snippet.vcf'
CHROMOSOME = '1'
NUCLEOTIDE = 'G'


@pytest.fixture
def temp_vcf_file():
    return VCF_FILE_PATH


def test_vcf_to_dataframe(temp_vcf_file):
    df = vcf_to_dataframe(temp_vcf_file)
    assert not df.empty
    assert list(df.columns) == ["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT", "NORMAL",
                                "TUMOUR"]


def test_validate_inputs_valid(temp_vcf_file):
    try:
        validate_inputs(temp_vcf_file, CHROMOSOME, NUCLEOTIDE)
    except ValueError:
        pytest.fail("validate_inputs() raised ValueError unexpectedly!")


def test_validate_inputs_invalid_vcf():
    with pytest.raises(ValueError):
        validate_inputs('invalid_file.vcf')


def test_validate_inputs_invalid_chromosome(temp_vcf_file):
    with pytest.raises(ValueError):
        validate_inputs(temp_vcf_file, '25')


def test_validate_inputs_invalid_nucleotide(temp_vcf_file):
    with pytest.raises(ValueError):
        validate_inputs(temp_vcf_file, CHROMOSOME, 'X')


def test_parse_all_snps(temp_vcf_file):
    with NamedTemporaryFile(delete=False, suffix='.csv') as temp_csv_file:
        output_csv = temp_csv_file.name
    parse_all_snps(temp_vcf_file, output_csv)
    df = pd.read_csv(output_csv)
    assert not df.empty
    os.remove(output_csv)


def test_parse_snps_by_chromosome(temp_vcf_file):
    df = parse_snps_by_chromosome(temp_vcf_file, CHROMOSOME)
    assert not df.empty
    assert all(df['CHROM'] == CHROMOSOME)


def test_parse_snps_by_chromosome_and_nucleotide(temp_vcf_file):
    df = parse_snps_by_chromosome_and_nucleotide(temp_vcf_file, CHROMOSOME, NUCLEOTIDE)
    assert not df.empty
    assert all(df['CHROM'] == CHROMOSOME)
    assert any(df['REF'] == NUCLEOTIDE) or any(df['ALT'] == NUCLEOTIDE)


def test_parse_significant_snps(temp_vcf_file):
    df = parse_significant_snps(temp_vcf_file, CHROMOSOME, NUCLEOTIDE)
    assert all(df['CHROM'] == CHROMOSOME)
    assert all(df['NORMAL_PVAL'] < 0.05)
