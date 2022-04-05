
# Define the bases
nucleotides = ["A", "C", "G", "T"]

# Check the sequence to ensure it is a DNA string
def validateSeq(seq):
    tmpseq = seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq

