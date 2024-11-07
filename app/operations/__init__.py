def addition(a: float, b: float) -> float:
    """
    Adds two numbers and returns the sum.
    """
    return a + b

def subtraction(a: float, b: float) -> float:
    """
    Subtracts the second number from the first and returns the result.
    """
    return a - b

def multiplication(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the product.
    """
    return a * b

def division(a: float, b: float) -> float:
    """
    Divides the first number by the second and returns the quotient.
    Raises ValueError if the second number is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def power(a: float, b: float) -> float:
    """
    Returns the result of raising the first number to the power of the second.
    """
    return a ** b

def modulus(a: float, b: float) -> float:
    """
    Returns the remainder of dividing the first number by the second.
    """
    return a % b