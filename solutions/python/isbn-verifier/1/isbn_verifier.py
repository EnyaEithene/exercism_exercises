def is_valid(isbn):
    isbn_noDashes = isbn.replace("-","")
    if len(isbn_noDashes) != 10:
        return False

    check = 0
    for i,digit in enumerate(isbn_noDashes):
        if digit in "0123456789":
            digit = int(digit)
        elif digit == "X" and i == len(isbn_noDashes) - 1:
            digit = 10
        else:
            return False
        check += digit * (10 - i)
    return check % 11 == 0
        
