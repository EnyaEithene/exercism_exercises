def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    total = 0
    i = 1
    while i <= 64:
        total += square(i)
        i += 1
    return total
