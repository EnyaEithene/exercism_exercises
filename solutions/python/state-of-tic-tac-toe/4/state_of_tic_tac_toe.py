def is_winning(string):
    """Checks whether the string is a win for any of the players
    INPUT:
        string (string): The 3-character sequence from the board

    OUTPUT:
        list: Contains whether it's a win to be added and by who
    """
    winning_conditions = ["XXX","OOO"]    # Conditions for winning the game
    
    if string in winning_conditions:
        return [1,string[0]]
    return [0,""]


def gamestate(board):
    """Checks the gamestate of a tic-tac-toe game board
    INPUT:
        board (list): How the board looks at the moment, each item representing a row

    OUTPUT:
        string: The state of the game (win, draw, ongoing, or error)
    """

    # ----- VARIABLES -----
    winning_stats = [0,""]                # Stats of winning (no. of wins, winners)

    # Strings to store more info about the board
    columns = ["","",""]                  # Stores columns from the board
    diagonals = ["",""]                   # Stores diagonals from the board

    # Counters of Xs and Os to check for invalid games
    count_x = 0
    count_o = 0

    # ----- BOARD ANALYSIS -----
    for index,row in enumerate(board):
        # Counters
        count_x += row.count("X")
        count_o += row.count("O")

        # Wins per line
        winning_stats = [stat + add_stat for stat, add_stat in zip(winning_stats, is_winning(row))]

        # Building columns, diagonals
        for index_col, column in enumerate(row):
            columns[index_col] += column
        diagonals[0] += row[index]
        diagonals[1] += row[-1-index]

    # ----- ADDITIONAL WIN CHECKS -----
    # Columns
    for column in columns:
        winning_stats = [stat + add_stat for stat, add_stat in zip(winning_stats, is_winning(column))]

    # Diagonals
    for diagonal in diagonals:
        winning_stats = [stat + add_stat for stat, add_stat in zip(winning_stats, is_winning(diagonal))]

    # ----- INVALID GAMES -----  
    # If X starts, O can't have more moves on the board then X
    if count_x < count_o:
        raise ValueError("Wrong turn order: O started")

    # X went twice
    if count_x >= count_o + 2:
        raise ValueError("Wrong turn order: X went twice")

    # Game should've ended after the game was won
    if winning_stats[0] > 1 and ("X" in winning_stats[1] and "O" in winning_stats[1]):
        raise ValueError("Impossible board: game should have ended after the game was won")

    # ----- STATE OF VALID GAME -----
    match winning_stats[0]:
        case 0 if count_o + count_x < 9:
            return "ongoing"
        case 0 if count_o + count_x == 9:
            return "draw"
        case 1:
            return "win"
        case 2 if "X" in winning_stats[1] or "O" in winning_stats[1]:
            return "win"