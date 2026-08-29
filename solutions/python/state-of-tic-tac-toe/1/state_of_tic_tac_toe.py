def gamestate(board):
    """Checks the gamestate of a tic-tac-toe game board
    INPUT:
        board (list): How the board looks at the moment, each item representing a row

    OUTPUT:
        string: The state of the game (win, draw, ongoing, or error)
    """

    # ----- VARIABLES -----
    wins = 0                 # Number of wins
    winners = ""             # Detected winners

    # Strings to store more info about the board
    columns = ["","",""]     # Stores columns from the board
    diagonals = ["",""]      # Stores diagonals from the board

    # Counters of Xs and Os to check for invalid games
    count_X = 0
    count_O = 0

    # ----- BOARD ANALYSIS -----
    for index,row in enumerate(board):
        # Counters
        count_X += row.count("X")
        count_O += row.count("O")

        # Wins per line
        if row in ("XXX","OOO"):
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
        if column in ("XXX","OOO"):
            wins += 1
            winners += row[0]

    # Diagonals
    for diagonal in diagonals:
        if diagonal in ("XXX","OOO"):
            wins += 1
            winners += row[0]

    # ----- INVALID GAMES -----
    # If X starts, O can't have more moves on the board then X
    if count_X < count_O:
        raise ValueError("Wrong turn order: O started")

    # X went twice
    if count_X >= count_O + 2:
        raise ValueError("Wrong turn order: X went twice")

    # Game should've ended after the game was won
    if wins > 1 and ("X" in winners and "O" in winners):
        raise ValueError("Impossible board: game should have ended after the game was won")

    # ----- STATE OF VALID GAME -----
    match wins:
        case 0 if count_O + count_X < 9:
            return "ongoing"
        case 0 if count_O + count_X == 9:
            return "draw"
        case 1:
            return "win"
        case 2 if "X" in winners or "O" in winners:
            return "win"