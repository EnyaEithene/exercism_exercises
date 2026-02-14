def is_armstrong_number(number):
    total = 0
    digits = len(str(abs(number)))
    number1 = number
    while number1:
        total += int(number1%10) ** digits
        number1 = number1 // 10
    if total == number:
        return True
    return False
