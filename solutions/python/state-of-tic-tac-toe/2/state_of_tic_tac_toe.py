def gamestate(board):
    """Checks the gamestate of a tic-tac-toe game board
    INPUT:
        board (list): How the board looks at the moment, each item representing a row

    OUTPUT:
        string: The state of the game (win, draw, ongoing, or error)
    """

    # ----- VARIABLES -----
    wins = 0                              # Number of wins
    winners = ""                          # Detected winners
    winning_conditions = ["XXX","OOO"]    # Conditions for winning the game

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
        if row in winning_conditions:
            wins += 1
            winners += row[0]

        # Building columns, diagonals
        for index_col, column in enumerate(row):
            columns[index_col] += column
        diagonals[0] += row[index]
        diagonals[1] += row[-1-index]

    # ----- ADDITIONAL WIN CHECKS -----
    # Columns
    for column in columns:
        if column in winning_conditions:
            wins += 1
            winners += column[0]

    # Diagonals
    for diagonal in diagonals:
        if diagonal in winning_conditions:
            wins += 1
            winners += diagonal[0]

    # ----- INVALID GAMES -----
    # If X starts, O can't have more moves on the board then X
    if count_x < count_o:
        raise ValueError("Wrong turn order: O started")

    # X went twice
    if count_x >= count_o + 2:
        raise ValueError("Wrong turn order: X went twice")

    # Game should've ended after the game was won
    if wins > 1 and ("X" in winners and "O" in winners):
        raise ValueError("Impossible board: game should have ended after the game was won")

    # ----- STATE OF VALID GAME -----
    match wins:
        case 0 if count_o + count_x < 9:
            return "ongoing"
        case 0 if count_o + count_x == 9:
            return "draw"
        case 1:
            return "win"
        case 2 if "X" in winners or "O" in winners:
            return "win"