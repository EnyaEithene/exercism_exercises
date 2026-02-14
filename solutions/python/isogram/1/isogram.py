def is_isogram(string):
    letters = []
    symbols = " -'"
    string = string.lower()
    for i in string:
        if i not in letters:
            letters += i
        elif i not in symbols:
            return False
    return True
