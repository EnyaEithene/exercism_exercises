def is_paired(input_string):
    """Checks if all the brackets inside the string are paired correctly
    INPUT:
        input_string (string): The string that needs checking

    OUTPUT:
        bool: Whether the brackets are paired correctly (True) or not (False)
    """
    if input_string == "":
        return True

    pairing_check = []
    # Dictionary to search for the right opener for a closer
    bracket_dictionary = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    # Searching the pairs
    for character in input_string:
        # Save brackets that need closing
        if character in {"{","[","("}:
            pairing_check.append(character)

        # Found closer bracket
        if character in {"}","]",")"}:
            # Delete opening bracket if we found its pair, else the pairing is wrong
            if not pairing_check:
                return False
            if bracket_dictionary[character] == pairing_check[-1]:
                pairing_check.pop()
            else:
                return False

    # Pairing is wrong if we didn't find pairs for all of the opening brackets
    if pairing_check:
        return False
    return True
