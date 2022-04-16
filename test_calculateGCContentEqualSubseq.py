import pytest
from dna_toolkit import calculateGCContentEqualSubseq


def test_for_string_with_default_k():
    assert calculateGCContentEqualSubseq("TCGATAGATAGCTACAG") == [30, 57]
    # exact value is [30, 57.1428...]

def test_for_string_shorter_than_k():
    assert calculateGCContentEqualSubseq("ATCAGGCTCACGGTA", k=20) == [53]
    # exact value is [53.3333...]

def test_for_string_equal_to_k():
    assert calculateGCContentEqualSubseq("CTTGATAGATCAGCTACAT", k=19) == [37]
    # exact value is [36.8421...]

def test_for_string_between_k_and_2k():
    assert calculateGCContentEqualSubseq("TCGATAGATAGCTACAG", k=10) == [30, 57]
    # exact value is [30, 57.1428...]

def test_for_string_equal_to_2k():
    assert calculateGCContentEqualSubseq("AATCGATAGATAGCCACCTTGCGAACATCG", k=15) == [40, 53]
    # exact value is [40, 53.3333...]

def test_for_string_equal_to_5k():
    assert calculateGCContentEqualSubseq("ATCGATATAACACGTCGCGATATTG", k=5) == [40, 0, 60 , 80, 20]

def test_for_string_between_5k_and_6k():
    assert calculateGCContentEqualSubseq("ATCGATATAACACGTCGCGATATTGCATG", k=5) == [40, 0, 60 , 80, 20, 50]
