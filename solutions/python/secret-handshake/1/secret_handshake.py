def commands(binary_str):
    """Takes a binary string and creates a secret handshake
    INPUT:
        binary_str (string): The number that is the basis of the handshake

    OUTPUT:
        list of strings: The gestures that need to be done as the secret handshake
    """

    handshake = []
    handshake_actions = ["wink", "double blink", "close your eyes", "jump"]

    for index,digit in enumerate(reversed(binary_str)):
        match digit:
            case '0':                                            # No action to be done
                continue
            case '1' if index < 4:                               # Action to be added
                handshake.append(handshake_actions[index])
            case '1' if index == 4:                              # Order of actions needs reversal
                handshake.reverse()
            case _:
                break

    return handshake