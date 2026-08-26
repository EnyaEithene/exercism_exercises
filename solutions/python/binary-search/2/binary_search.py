def find(search_list, value):
    """Finds a value in a list using the binary method
    Input:
        search_list (list[int]): List in which we search the value
        value (int): The value we're searching for

    Output:
        int: The position where the value is found or error otherwise
    """
    
    search_list_copy = list(search_list)
    while search_list:
        # Only one element and it's not the one we're searching for
        if len(search_list) == 1 and search_list[0] != value:    
            break
            
        middle = len(search_list) // 2    # Find middle of list

        # Found the value
        if search_list[middle] == value:    
            return search_list_copy.index(value)

        # Didn't find the value
        # Delete right of list if values are too high
        if search_list[middle] > value:    
            del search_list[middle:]
        # Delete left of list if values are too low
        elif search_list[middle] < value:    
            del search_list[:middle]
            
    raise ValueError("value not in array")
