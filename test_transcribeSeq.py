import pytest
from dna_toolkit import transcribeSeq


def test_for_thymine_only_sequence():
    assert transcribeSeq("TTTTT") == "UUUUU"

def test_for_sequence_without_thymine():
    assert transcribeSeq("ACGGCGAGGGGCCCA") == "ACGGCGAGGGGCCCA"

def test_for_arbitrary_sequence():
    assert transcribeSeq("ACTCCGTCAGACGGCTTAAG") == "ACUCCGUCAGACGGCUUAAG"
