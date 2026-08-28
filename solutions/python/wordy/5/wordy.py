def is_number(word):
    """Checks if in string is a real number
    INPUT:
        word (str): The string we need to check

    OUTPUT:
        bool: If it is a number and can be turned into one or not
    """
    
    try:
        int(word)
        return True
    except ValueError:
        return False
        

def answer(question):
    """Answers mathematical question
    INPUT:
        question (str): The mathematical problem that needs solving

    OUTPUT:
        int: The solution to the problem
    """

    # Cleaning up the question
    question = question.removeprefix("What is ")
    question = question.rstrip("?")
    question_words = question.split(" ")
    
    # First number
    if is_number(question_words[0]):
        result = int(question_words[0])
        question_words = question_words[1:]
    else:
        # Give error if we can't start the equation with a number
        raise ValueError("syntax error")

    # Solve operations if they exist
    while question_words:
        match question_words:
            # Addition
            case ["plus", number, *rest] if is_number(number):
                result += int(number)
                question_words = rest

            # Subtraction
            case ["minus", number, *rest] if is_number(number):
                result -= int(number)
                question_words = rest

            # Multiplication
            case ["multiplied", "by", number, *rest] if is_number(number):
                result *= int(number)
                question_words = rest

            # Division
            case ["divided", "by", number, *rest] if is_number(number):
                result /= int(number)
                question_words = rest

            # Incomplete operation
            case ["plus", *_] | ["minus", *_] | ["multiplied", *_] | ["divided", *_]:
                raise ValueError("syntax error")

            # Double number
            case [number, *_] if is_number(number):
                raise ValueError("syntax error")

            # Unknown operation
            case _:
                raise ValueError("unknown operation")

    return result