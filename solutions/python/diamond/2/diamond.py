def rows(letter):
    """Creates a diamond of a size dictated by the letter given
    INPUT:
        letter (string): The letter used to print the diamond with

    OUTPUT:
        list: Every row of the diamond that results
    """
    letter_code = ord(letter)                        # Find the ASCII code of the letter given
    a_code = ord("A")                                # ASCII code of letter "A"
    diamond_size = letter_code - a_code              # Size of diamond (how many letters to use - 1)

    # Creating the diamond
    diamond = []

    # First row
    diamond.append(" " * diamond_size
                           + chr(a_code) 
                           + " " * diamond_size)
    
    if diamond_size != 0:
        # Top middle
        for index in range(diamond_size):
            diamond.append(" " * (diamond_size - index - 1) 
                                + chr(a_code + index + 1) 
                                + " " * (index*2 + 1)
                                + chr(a_code + index + 1) 
                                + " " * (diamond_size - index - 1))
        # Top bottom
        for index in range(diamond_size - 1, 0, -1):
            diamond.append(" " * (diamond_size - index) 
                                + chr(a_code + index) 
                                + " " * (index*2 - 1)
                                + chr(a_code + index) 
                                + " " * (diamond_size - index))     
        # Last row
        diamond.append(" " * diamond_size
                            + chr(a_code) 
                            + " " * diamond_size)
        
    return diamond
