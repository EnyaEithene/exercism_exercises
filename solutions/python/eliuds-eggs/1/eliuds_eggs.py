def egg_count(display_value):
    """Finds number of actual eggs in the coup
    Input:
        display_value (int): Number displayed in decimal

    Output:
        int: Number of actual eggs in coup based on the binary of the decimal number
    """

    # Transform value from decimal to binary to find egg positions
    positions = []
    while display_value:
        positions.append(display_value % 2)
        display_value = display_value // 2

    # Give sum of egg positions (counts each existing egg)
    return sum(positions)
        