import pytest
from dna_toolkit import generateReverseComplement


def test_for_simple_string():
    assert generateReverseComplement("ACGT") == "ACGT"

def test_for_three_nucleotide_string():
    assert generateReverseComplement("GACCAAAGGC") == "GCCTTTGGTC"

def test_for_arbitrary_string():
    assert generateReverseComplement("ACTCCGTCAGACGGCTTAAG") == "CTTAAGCCGTCTGACGGAGT"
