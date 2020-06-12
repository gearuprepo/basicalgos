# O(n) =n 
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    retmin = 0
    retmax = 0
    for i in ints:
        if i<retmin:
            retmin = i
        if i>retmax:
            retmax = i
    return retmin,retmax

## Example Test Case of Ten Integers
print("Test case 1")
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print("Test case 2")
inp = [3,44,64,1,-1,0,49,39,7,33]
print ("Pass" if ((-1, 64) == get_min_max(inp)) else "Fail")
