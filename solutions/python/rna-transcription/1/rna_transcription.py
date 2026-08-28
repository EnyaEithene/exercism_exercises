def to_rna(dna_strand):
    """It finds the RNA complement of the DNA strand given
    INPUT:
        dna_strand (str): The DNA strand for which we need to determine the RNA complement
    
    OUTPUT:
        str: The determined RNA complement
    """

    # Dictionary that contains the complements
    rna_complement = {"G": "C",
                     "C": "G",
                     "T": "A",
                     "A": "U"}
    rna_strand = ""

    # Creating the RNA complement from the given dna_strand
    for letter in dna_strand:
        rna_strand = rna_strand + rna_complement[letter]

    return rna_strand