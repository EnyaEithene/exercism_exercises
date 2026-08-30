def is_float_useful(number):
    """Checks whether the float format is useful; if not, turn to integer
    INPUT:
        number (float): A number in a float format (eg. 4.5, 1.0, etc.)

    OUTPUT:
        float/integer: Keep it as a float if the information is useful (eg. 4.5), or turn it into an integer if not (eg. 1,0)
    """
    return int(number) if number.is_integer() else number

def resistor_label(colors):
    """Reads labels from resistors

    Param:
        colors (list): The colors of the bands from the resistor

    Output:
        number: Value of resistor in ohms and the tolerances
    """

    # ----- VARIABLES -----
    number = 0        # Value of resistor
    result = ""       # The final value of resistor based on the labels given

    # Lists for the colored bands on the resistor
    # - for value and multiplier band
    color_list = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    # - for tolerance band
    tolerance_dict = {"grey": 0.05,
                     "violet": 0.1,
                     "blue": 0.25,
                     "green": 0.5,
                     "brown": 1,
                     "red": 2,
                     "gold": 5,
                     "silver": 10}

    # ----- VALUE IN OHMS -----
    # When there's only one band
    if len(colors) == 1:
        return f"{color_list.index(colors[0])} ohms"
    
    # Find values
    for index, color in enumerate(colors):
        if index < len(colors) - 2:
            number = number * 10 + color_list.index(color)
        elif index == len(colors) - 2:
            number = number * (10 ** color_list.index(color))

    # Translate in ohms
    if number < 1_000:
        result = f"{is_float_useful(number)} ohms"
    elif number < 1_000_000:
        result = f"{is_float_useful(number/1_000)} kiloohms"
    elif number < 1_000_000_000:
        result = f"{is_float_useful(number/1_000_000)} megaohms"
    else:
        result = f"{is_float_useful(number/1_000_000_000)} gigaohms"

    # Add tolerance to result
    result += f" ±{tolerance_dict[colors[-1]]}%"

    # Return final reading
    return result