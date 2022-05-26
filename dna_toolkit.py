import structures as strc
import collections as coll


# Check the sequence to ensure it is a DNA string
def validateSeq(seq):
    """
    Check if sequence is valid DNA string.

    Args:
        seq (str): DNA string

    Returns:
        seq in uppercase (str) if seq is valid
        False (bool) if seq is invalid or empty
    """
    if len(seq) == 0:
        return False
    tmpseq = seq.upper()
    for nuc in tmpseq:
        if nuc not in strc.nucleotides:
            return False
    return tmpseq


# Count the frequency of each nucleotide in the DNA string
def countNucFrequency(seq):
    """
    Count frequency of each nucleotide in DNA string.

    Args:
        seq (str): DNA string

    Returns:
        Frequency of each nucleotide (dict)
    """
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
    """
    Perform transcription of DNA string: DNA -> RNA.

    Args:
        seq (str): DNA string

    Returns:
        seq with Thymine [T] replaced with Uracil [U] (str)
    """
    # Make sure to run validateSeq() before running this function
    return seq.replace("T", "U")


# Generate the reverse complement of a DNA string
def generateReverseComplement(seq):
    """
    Generate reverse complement of DNA string.

    Args:
        seq (str): DNA string

    Returns:
        reversed seq with
        Thymine [T] swapped with Adenine [A] and
        Guanine [G] swapped with Cytosine [C] (str)

    """
    # Make sure to run validateSeq() before running this function
    complementSeq = "".join(strc.nucleotideComplements[nuc] for nuc in seq)
    return complementSeq[::-1]


# Calculate the GC content of a DNA or RNA string
def calculateGCContent(seq, start=None, end=None):
    """
    Calculate GC content of DNA or RNA string,
    i.e. percentage of bases that are Guanine
    or Cytosine.

    Args:
        seq (str): DNA or RNA string
        start (int) [Optional]: index within seq where calculation starts
        end (int) [Optional]: index within seq where calculation ends

    Returns:
        GC content of seq or segment of seq defined by start and end (float)
    """
    return round((seq.count("G", start, end) + seq.count("C", start, end)) / len(seq[start:end]) * 100)


# Calculate the GC content of subsequences of a DNA or RNA string that are of equal length
def calculateGCContentEqualSubseq(seq, k=10):
    """
    Calculate GC content of subsequences of DNA or RNA string
    that are of equal length.

    Args:
        seq (str): DNA or RNA string
        k (int) [Optional]: length of subsequence (default value = 10)

    Returns:
        GC content of each subsequence (list)
        If last subsequence is shorter than k, last entry
        is simply GC content of that subsequence.
    """
    subseqGCContent = []
    front = 0
    seqLen = len(seq)
    while front < seqLen:
        end = front + k
        if end >= seqLen:
            end = seqLen
        subseqGCContent.append(calculateGCContent(seq, front, end))
        front += k
    return subseqGCContent


# Translate a DNA string: DNA -> ... -> amino acid sequence
def translateSeq(seq, initPos=0):
    """
    Perform translation of DNA string: DNA -> ... -> amino acid sequence

    Args:
        seq (str): DNA string
        initPos (int) [Optional]: index within seq where translation starts

    Returns:
        sequence of amino acids corresponding to seq (str)
    """
    return [strc.DNACodons[seq[pos:pos+3]] for pos in range(initPos, len(seq), 3) if (len(seq)-pos)>=3]


# Calculate the frequency of each codon encoding a particular amino acid in a DNA string
def calculateCodonUsage(seq, aminoAcid):
    """
    Calculate frequency of each codon encoding particular amino acid in DNA string

    Args:
        seq (str): DNA string
        aminoAcid (char): amino acid

    Returns:
        frequency of each codon encoding aminoAcid (dict)
    """
    tmpList = []
    for pos in range(0, len(seq)-2, 3):
        if strc.DNACodons[seq[pos:pos+3]] == aminoAcid:
            tmpList.append(seq[pos:pos+3])

    freqDict = dict(coll.Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
    return freqDict
