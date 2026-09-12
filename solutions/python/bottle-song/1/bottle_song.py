def recite(start, take=1):
    """Recites the specified paragraphs of the song "Ten Green Bottles"
    INPUT:
        start (integer): The number of bottles at which the song will start at
        take (integer): The number of bottles to take from the starting number

    OUTPUT:
        list of strings: The song paragraphs that were asked for
    """

    # The base of the song: the repetitive lyrics and the numbers
    lyrics = [" green bottles hanging on the wall,",
              " green bottle hanging on the wall,",
             "And if one green bottle should accidentally fall,",
             "There'll be ",
             " green bottles hanging on the wall.",
             " green bottle hanging on the wall."]

    numbers = {10: "Ten",
              9: "Nine",
              8: "Eight",
              7: "Seven",
              6: "Six",
              5: "Five",
              4: "Four",
              3: "Three",
              2: "Two",
              1: "One",
              0: "no"}

    # Creating the recital
    recital = []
    for bottle_number in range(start, start - take, -1):
        # First two verses
        if bottle_number > 1:
            recital.append((numbers[bottle_number] + lyrics[0]))
            recital.append((numbers[bottle_number] + lyrics[0]))
        else:
            recital.append((numbers[bottle_number] + lyrics[1]))
            recital.append((numbers[bottle_number] + lyrics[1]))

        # Third verse
        recital.append((lyrics[2]))

        # Fourth verse
        if bottle_number - 1 > 1 or bottle_number - 1 == 0:
            recital.append((lyrics[3] + (numbers[bottle_number - 1]).casefold() + lyrics[4]))
        else:
            recital.append((lyrics[3] + (numbers[bottle_number - 1]).casefold() + lyrics[5]))

        # Add delimiter between paragraphs
        if bottle_number != start - take + 1:
            recital.append((""))

    return recital