import pytest
from dna_toolkit import calculateCodonUsage


def test_for_no_corresponding_codons():
    seq = "CGATGGCATTACGC"
    assert calculateCodonUsage(seq, '_') == {}

def test_for_one_codon_only():
    seq = "CTTATGATGGCTATGCCGTACATG"
    assert calculateCodonUsage(seq, 'M') == {"ATG": 1.0}

def test_for_amino_acid_L():
    seq = "TTA" + \
          "GCC" + "TTA" + "GCA" + \
          "GGC" + "TTA" + \
          "GCT" + "CTT" + "CTT" + \
          "GCG" + "GCC" + "GCG" + "GCG" + \
          "CTT"
    assert calculateCodonUsage(seq, 'L') == {"TTA": 0.5, "CTT": 0.5}

def test_for_amino_acid_A():
    seq = "ACT" + \
          "GCC" + "GCG" + "GCA" + \
          "GGC" + "TAC" + \
          "GCT" + "GCT" + "GCT" + \
          "GCG" + "GCC" + "GCG" + "GCG" + \
          "TAT" + "AC"
    assert calculateCodonUsage(seq, 'A') == {"GCC": 0.2, "GCG": 0.4, "GCA": 0.1, "GCT": 0.3}
