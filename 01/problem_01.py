import math
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    
    x = number  
    tolerance = 1
    guess = recursqrt(x,number,tolerance)
    return math.floor(guess)

def recursqrt(x, number, tolerance):
    guess = 0.5 * (x + number/x)
    if abs(guess - x) < tolerance:
        return guess
    else:
        return recursqrt(guess,number,tolerance)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (10 == sqrt(100)) else "Fail")