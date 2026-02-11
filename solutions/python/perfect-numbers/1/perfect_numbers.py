def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    total = 0
    for i in range(1,number//2+1):
        total += i if number % i == 0 else 0

    if total == number:
        return "perfect"
    if total > number:
        return "abundant"
    return "deficient"