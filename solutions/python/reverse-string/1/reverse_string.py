def reverse(text):
    """Reverses the string of text given
    INPUT:
        text (string): The original text that needs to be reversed

    OUTPUT:
        string: The reversed text
    """
    reversed_text = ""
    for letter in text[::-1]:
        reversed_text += letter

    return reversed_text
