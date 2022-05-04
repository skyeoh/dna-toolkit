from dna_toolkit import translateSeq


def test_for_repeating_DNA_sequence():
    assert translateSeq("ATCGATCGATCGATCGATCGATCG") == ['I', 'D', 'R', 'S', 'I', 'D', 'R', 'S']

def test_for_repeating_DNA_sequence_with_offset_1():
    assert translateSeq("ATCGATCGATCGATCGATCGATCG", 2) == ['R', 'S', 'I', 'D', 'R', 'S', 'I']

def test_for_repeating_DNA_sequence_with_offset_2():
    assert translateSeq("ATCGATCGATCGATCGATCGATCG", 4) == ['I', 'D', 'R', 'S', 'I', 'D']

def test_for_all_amino_acids():
    seq = "GCT" + "GCC" + "GCA" + "GCG" + \
            "TGT" + "TGC" + \
            "GAT" + "GAC" + \
            "GAA" + "GAG" + \
            "TTT" + "TTC" + \
            "GGT" + "GGC" + "GGA" + "GGG" + \
            "CAT" + "CAC" + \
            "ATA" + "ATT" + "ATC" + \
            "AAA" + "AAG" + \
            "TTA" + "TTG" + "CTT" + "CTC" + "CTA" + "CTG" + \
            "ATG" + \
            "AAT" + "AAC" + \
            "CCT" + "CCC" + "CCA" + "CCG" + \
            "CAA" + "CAG" + \
            "CGT" + "CGC" + "CGA" + "CGG" + "AGA" + "AGG" + \
            "TCT" + "TCC" + "TCA" + "TCG" + "AGT" + "AGC" + \
            "ACT" + "ACC" + "ACA" + "ACG" + \
            "GTT" + "GTC" + "GTA" + "GTG" + \
            "TGG" + \
            "TAT" + "TAC" + \
            "TAA" + "TAG" + "TGA"
    assert translateSeq(seq) == ['A', 'A', 'A', 'A', 'C', 'C', 'D', 'D', 'E', 'E', \
                                 'F', 'F', 'G', 'G', 'G', 'G', 'H', 'H', 'I', 'I', \
                                 'I', 'K', 'K', 'L', 'L', 'L', 'L', 'L', 'L', 'M', \
                                 'N', 'N', 'P', 'P', 'P', 'P', 'Q', 'Q', 'R', 'R', \
                                 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'S', 'S', \
                                 'T', 'T', 'T', 'T', 'V', 'V', 'V', 'V', 'W', 'Y', \
                                 'Y', '_', '_', '_']

def test_for_all_amino_acids_with_offset_1():
    seq = "GCT" + "GCC" + "GCA" + "GCG" + \
            "TGT" + "TGC" + \
            "GAT" + "GAC" + \
            "GAA" + "GAG" + \
            "TTT" + "TTC" + \
            "GGT" + "GGC" + "GGA" + "GGG" + \
            "CAT" + "CAC" + \
            "ATA" + "ATT" + "ATC" + \
            "AAA" + "AAG" + \
            "TTA" + "TTG" + "CTT" + "CTC" + "CTA" + "CTG" + \
            "ATG" + \
            "AAT" + "AAC" + \
            "CCT" + "CCC" + "CCA" + "CCG" + \
            "CAA" + "CAG" + \
            "CGT" + "CGC" + "CGA" + "CGG" + "AGA" + "AGG" + \
            "TCT" + "TCC" + "TCA" + "TCG" + "AGT" + "AGC" + \
            "ACT" + "ACC" + "ACA" + "ACG" + \
            "GTT" + "GTC" + "GTA" + "GTG" + \
            "TGG" + \
            "TAT" + "TAC" + \
            "TAA" + "TAG" + "TGA"
    assert translateSeq(seq, 1) == ['L', 'P', 'Q', 'R', 'V', 'A', 'M', 'T', 'K', 'S', \
                                    'F', 'S', 'V', 'A', 'E', 'G', 'I', 'T', '_', 'L', \
                                    'S', 'K', 'S', 'Y', 'C', 'F', 'S', 'Y', '_', '_', \
                                    'I', 'T', 'L', 'P', 'H', 'R', 'N', 'S', 'V', 'A', \
                                    'D', 'G', 'E', 'G', 'L', 'P', 'H', 'R', 'V', 'A', \
                                    'L', 'P', 'Q', 'R', 'L', 'S', '_', 'C', 'G', 'I', \
                                    'T', 'N', 'S']

def test_for_all_amino_acids_with_offset_2():
    seq = "GCT" + "GCC" + "GCA" + "GCG" + \
            "TGT" + "TGC" + \
            "GAT" + "GAC" + \
            "GAA" + "GAG" + \
            "TTT" + "TTC" + \
            "GGT" + "GGC" + "GGA" + "GGG" + \
            "CAT" + "CAC" + \
            "ATA" + "ATT" + "ATC" + \
            "AAA" + "AAG" + \
            "TTA" + "TTG" + "CTT" + "CTC" + "CTA" + "CTG" + \
            "ATG" + \
            "AAT" + "AAC" + \
            "CCT" + "CCC" + "CCA" + "CCG" + \
            "CAA" + "CAG" + \
            "CGT" + "CGC" + "CGA" + "CGG" + "AGA" + "AGG" + \
            "TCT" + "TCC" + "TCA" + "TCG" + "AGT" + "AGC" + \
            "ACT" + "ACC" + "ACA" + "ACG" + \
            "GTT" + "GTC" + "GTA" + "GTG" + \
            "TGG" + \
            "TAT" + "TAC" + \
            "TAA" + "TAG" + "TGA"
    assert translateSeq(seq, 2) == ['C', 'R', 'S', 'V', 'L', 'R', '_', 'R', 'R', 'V', \
                                    'F', 'R', 'W', 'R', 'R', 'A', 'S', 'H', 'N', 'Y', \
                                    'Q', 'K', 'V', 'I', 'A', 'S', 'P', 'T', 'D', 'E', \
                                    '_', 'P', 'S', 'P', 'T', 'A', 'T', 'A', 'S', 'P', \
                                    'T', 'E', 'K', 'V', 'F', 'L', 'I', 'E', '_', 'H', \
                                    'Y', 'H', 'N', 'G', 'C', 'R', 'S', 'V', 'V', 'L', \
                                    'L', 'I', 'V']
