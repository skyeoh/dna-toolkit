import pytest
from dna_toolkit import countNucFrequency


def test_for_one_nucleotide_string():
    assert countNucFrequency("GGGG") == {"G": 4}

def test_for_two_nucleotide_string():
    assert countNucFrequency("AGGGAG") == {"A": 2, "G": 4}

def test_for_three_nucleotide_string():
    assert countNucFrequency("AGTTGGTAGTT") == {"T": 5, "A": 2, "G": 4}

def test_for_ascending_frequency_string():
    assert countNucFrequency("ATTCCCGGGG") == {"A": 1, "T": 2, "C": 3, "G": 4}

def test_for_descending_frequency_string():
    assert countNucFrequency("GGGGCCCTTA") == {"A": 1, "T": 2, "C": 3, "G": 4}

def test_for_cyclical_string():
    assert countNucFrequency("ACGTACGTACGTACGT") == {"A": 4, "T": 4, "C": 4, "G": 4}
