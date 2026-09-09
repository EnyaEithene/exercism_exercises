def distance(strand_a, strand_b):
    """Calculates the hamming distantce between two DNA strands
    INPUT:
        strand_a (string): The first DNA strand of the comparison
        strand_b (string): The second DNA strand of the comparison

    OUTPUT:
        integer: The resulted Hamming distance between the two (the number of differences)
    """

    # Error in case the strands aren't of the same length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    hamming_distance = 0

    # We count the amount of instances where the two strands don't match
    for index, letter in enumerate(strand_a):
        if letter != strand_b[index]:        
            hamming_distance += 1

    return hamming_distance