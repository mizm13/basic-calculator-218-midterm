from typing import Union

# Define a type alias for numbers (both int and float)

Number = Union[int, float]

# addition function 
def addition(a: Number, b: Number) -> Number:
    """
    This function takes two numbers as arguments and returns their sum.
    
    Arguments:
    a -- The first number (float or int)
    b -- The second number (float or int)
    """
    return a + b  # Return the sum of a and b

# subtraction function
def subtraction(a: Number, b: Number) -> Number:
    """
    This function takes two numbers as arguments and returns the result of subtracting b from a.
    
    Arguments:
    a -- The first number (float or int)
    b -- The second number (float or int)
    """
    return a - b  # Return the result of a minus b

def multiplication(a: Number, b: Number) -> Number:
    """
    This function takes two numbers as arguments and returns their product.
    
    Arguments:
    a -- The first number (float or int)
    b -- The second number (float or int)
    """
    return a * b  # Return the product of a and b

def division(a: Number, b: Number) -> Number:
    """
    This function takes two numbers as arguments and returns the result of dividing a by b.
    
    Arguments:
    a -- The first number (float or int)
    b -- The second number (float or int)
    """
    return a / b  # Return the result of a divided by b