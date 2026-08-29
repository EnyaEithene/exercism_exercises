def count_neighbours(garden, garden_height, garden_width, x_pos, y_pos):
    """Counts how many flowers there are around the position of the EMPTY space (8 positions in an 3x3 grid, position being the center)
    INPUT:
        garden (list of strings): List with the rows of the garden with flowers (*) and empty spaces
        garden_height (int): The "height" of the garden => used for x_pos that is the row coordinate
        garden_width (int): The "width" of the garden => used for y_pos that is the column coordinate
        x_pos (int): The row in which the position of the EMPTY space is
        y_pos (int): The column in which the position of the EMPTY space is

    OUTPUT:
        string: The number of flowers surrounding the position of the EMPTY space
    """
    
    # Counter for neighbouring flowers
    counter = 0                       

    # Counting flowers from around the position of the EMPTY space
    for x_add in {-1,0,1}:
        for y_add in {-1,0,1}:
            # Needs to be within the garden and for the spot to have a flower
            if (0 <= x_pos + x_add < garden_height and 0 <= y_pos + y_add < garden_width) and garden[x_pos + x_add][y_pos + y_add] == "*":
                counter += 1

    # Return the number as a string or a whitespace per the original garden given
    return str(counter) if counter != 0 else " "
    

def annotate(garden):
    """Adds flower counts in the empty spaces of the garden given
    INPUT:
        garden (list of strings): List with the rows of the garden with flowers (*) and empty spaces

    OUTPUT:
        list: The same garden but with flower counts in squares that are surrounded by flowers
    """

    # ----- VARIABLES -----
    garden_counter = []               # The resulting flower count of the garden

    # If garden is empty
    if not garden:
        return garden_counter

    garden_height = len(garden)       # The "height" of the garden
    garden_width = len(garden[0])     # The "width" of the garden
    
    # ----- GENERATE EMPTY GARDEN COUNTER -----
    for row in garden:
        if len(row) != garden_width:
            raise ValueError("The board is invalid with current input.")
        garden_counter.append(list(" " * garden_width))

    # ----- COUNTING FLOWERS ------
    for row_index, row in enumerate(garden):
        for column_index, column in enumerate(row):
            match column:
                case "*":    # Found a flower
                    garden_counter[row_index][column_index] = "*"
                    
                case " ":    # Empty space => Check around it and count flowers 
                    garden_counter[row_index][column_index] = count_neighbours(garden, garden_height, garden_width, row_index, column_index)
                    
                case _:      # Found an invalid character
                    raise ValueError("The board is invalid with current input.") 

    # Return answer in proper format
    garden_counter = ["".join(row) for row in garden_counter]
    return garden_counter   
