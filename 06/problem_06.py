# O(n) =n 
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    #Fix1: Boundary condition fix
    retmin = ints[0]
    retmax = ints[0]
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

#egde case 1: large list with all postive numbers >0 
input = [i for i in range(3,20000)]   
print ("Pass" if ((min(input), max(input)) == get_min_max(input)) else "Fail")

#egde case 2: large list   with all negative numbers   
inp = ([i for i in range(-200000,-20000)])
print ("Pass" if ((min(inp), max(inp)) == get_min_max(inp)) else "Fail")
