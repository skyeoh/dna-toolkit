import pytest
from dna_toolkit import validateSeq


def test_for_valid_seq():
    assert validateSeq("ATTATGCGCCCAAAT") == "ATTATGCGCCCAAAT"

def test_for_valid_seq_with_upper_lower_cases():
    assert validateSeq("ATtAtGCgCcCAAaT") == "ATTATGCGCCCAAAT"

def test_for_invalid_seq():
    assert validateSeq("ATTATGCGCCCXAAT") == False

def test_for_invalid_seq_with_upper_lower_cases():
    assert validateSeq("ATtAtGCgCcCxAaT") == False

def test_for_empty_seq():
    assert validateSeq("") == False
