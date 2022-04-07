
# Define the bases
nucleotides = ["A", "C", "G", "T"]

# Check the sequence to ensure it is a DNA string
def validateSeq(seq):
    if len(seq) == 0:
        return False
    tmpseq = seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq

# Count the frequency of each nucleotide in the DNA string
def countNucFrequency(seq):
    # Make sure to run validateSeq() before running this function
    tmpFreqDict = {}
    for nuc in seq:
        if tmpFreqDict.get(nuc) is None:
            tmpFreqDict[nuc] = 1
        else:
            tmpFreqDict[nuc] += 1
    return tmpFreqDict

# Transcribe a DNA string: DNA -> RNA
def transcribeSeq(seq):
    # Make sure to run validateSeq() before running this function
    return seq.replace("T", "U")

