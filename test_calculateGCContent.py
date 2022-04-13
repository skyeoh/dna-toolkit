import pytest
from dna_toolkit import calculateGCContent


def test_for_string_with_all_G():
    assert calculateGCContent("GGGGG") == 100

def test_for_string_with_all_C():
    assert calculateGCContent("CCC") == 100

def test_for_string_with_all_GC():
    assert calculateGCContent("GGCCCGCGCCG") == 100

def test_for_string_with_no_GC():
    assert calculateGCContent("ATTTAATATT") == 0

def test_for_arbitrary_string_1():
    assert calculateGCContent("CCTATTTATTAAGTTAATCTACAGGCAC") == 32 # exact value is 32.1428...

def test_for_arbitrary_string_2():
    assert calculateGCContent("CCTATTTACCAAGTTAAGCTACAGGCAC") == 43 # exact value is 42.8571...
