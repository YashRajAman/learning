import math
from generic import check_util as check


def squareOf(x):
    """
    Funtion to provide squred product of a number.
    Argument x is the number. Supports only int and float
    """
    if check.is_instance_of_any(x, (int, float)):
        return x*x
    else:
        return None
    
def power(x,y):
    """
    Function to provide exponential multiplication.
    First arg x is base and second arg y is exponent.
    x to power y
    Supports only int and float
    """
    if check.is_instance_of_any(x, (int, float)) and check.is_instance_of_any(y, (int, float)):
        return x**y
    else:
        return None