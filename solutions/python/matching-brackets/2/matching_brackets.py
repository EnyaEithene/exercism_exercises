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
            if (pairing_check[-1] == "(" and character == ")") or (pairing_check[-1] == "[" and character == "]") or (pairing_check[-1] == "{" and character == "}"):
                pairing_check.pop()
            else:
                return False

    # Pairing is wrong if we didn't find pairs for all of the opening brackets
    if pairing_check:
        return False
    return True
