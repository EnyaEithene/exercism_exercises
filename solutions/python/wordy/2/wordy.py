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

    while question_words:
        if len(question_words) >= 3:
            if question_words[1] == "by" and is_number(question_words[2]):
                # Multiplication
                if question_words[0] == "multiplied":
                    result = result * int(question_words[2])
                    question_words = question_words[3:]
                    continue
        
                # Division
                if question_words[0] == "divided":
                    result = result / int(question_words[2])
                    question_words = question_words[3:]
                    continue
                    
        if len(question_words) >= 2:
            if is_number(question_words[1]):
                # Addition
                if question_words[0] == "plus":
                    result += int(question_words[1])
                    question_words = question_words[2:]
                    continue
        
                # Subtraction
                if question_words[0] == "minus":
                    result -= int(question_words[1])
                    question_words = question_words[2:]
                    continue

        # Unknown operation
        if len(question_words) == 1:
            if question_words[0] not in ("plus","minus") and not is_number(question_words[0]):
                raise ValueError("unknown operation")

        # Syntax error if no operation could be done
        raise ValueError("syntax error")

    return result