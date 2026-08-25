def rebase(input_base, digits, output_base):
    """ Transforms a number from a base to another
    
    Args:
        input_base (integer): Initial base
        digits (list): List of numbers in the initial base
        output_base (integer): The base the number needs to be translated into

    Returns:
        list: The original number given in digits, now changed in output_base
    """
    
    # Initial checks for base value (needs to be at least 2)
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Transform from input_base in base 10 to transit between bases
    number = 0
    for digit in digits:
        if 0 <= digit < input_base:
            number = number * input_base + digit
        else:
            raise ValueError("all digits must satisfy 0 <= d < input base") 

    # Transform from base 10 in output_base
    if number != 0:
        new_number = []
        while number:
            new_number.append(number%output_base)
            number = number // output_base
        return new_number[::-1]
    else:
        return [0]