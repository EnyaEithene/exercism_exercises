def encode(plain_text):
    """Encodes the plain_text given using the Atbash cipher
    INPUT:
        plain_text (str): The original message that needs to be encoded

    OUTPUT:
        str: The resulted encoded message
    """

    encoded_text = ""
    group_of_5_counter = 0
    for letter in plain_text.lower():
        # Boolean for if we added a letter or not to the message
        added_letter = False

        # Encode and add to encoded message if it is from the alphabet
        if letter.isalpha():
            encoded_text += chr(ord("z")-(ord(letter)-ord("a")))
            group_of_5_counter += 1
            added_letter = True
            
        # Encode and add to encoded message if it is a number
        if letter.isdigit():
            encoded_text += letter
            group_of_5_counter += 1
            added_letter = True

        # Add whitespace if group of five was formed after adding to the message
        if group_of_5_counter % 5 == 0 and encoded_text and added_letter:
                encoded_text += " "

    # Return the resulted message
    # - added strip() so it removes any trailing whitespaces that were added right at the end
    return encoded_text.strip()    


def decode(ciphered_text):
    """Decodes the ciphered_text into plain text using the Atbash cipher
    INPUT:
        ciphered_text (str): The text that needs decoding

    OUTPUT:
        str: The resulted decoded text
    """

    decoded_text = ""

    for letter in ciphered_text:
        if letter.isalpha():
            # Same logic as earlier, we mirror the character within the alphabet
            decoded_text += chr(ord("z")-(ord(letter)-ord("a")))    
        if letter.isdigit():
            decoded_text += letter

    return decoded_text
