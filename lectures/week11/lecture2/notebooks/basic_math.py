def add(a, b):
    """
    (number, number) -> number
    Return the sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    (number, number) -> number
    Return the difference of a and b.
    """
    return a - b


def multiply(a, b):
    """
    (number, number) -> number
    Return the product of a and b.
    """
    return a * b


def divide(a, b):
    """
    (number, number) -> number or str
    Return the result of a divided by b.
    If b is 0, return an error message.
    """
    if b == 0:
        return "Error. You cannot divide by zero."
    return a / b
