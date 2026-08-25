def label(colors):
    """Reads labels from resistors

    Param:
        colors (list): The colors of the bands from the resistor

    Output:
        number: Value of resistor in ohms
    """

    number = 0
    color_list = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

    # Find value of resistor
    for index, color in enumerate(colors):
        if index < 2:
            number = number * 10 + color_list.index(color)
        elif index == 2:
            number = number * (10 **color_list.index(color))

    # Translate in ohms
    if number < 1_000:
        return f"{number} ohms"
    elif number < 1_000_000:
        return f"{number//1_000} kiloohms"
    elif number < 1_000_000_000:
        return f"{number//1_000_000} megaohms"
    else:
        return f"{number//1_000_000_000} gigaohms"