#O(n) = log n
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    retval = recursearch(input_list,number,0)
    return retval


def recursearch(input_list,number,index):
    size = len(input_list)
    rightedgeindex = size - 1
    leftedgeindex = 0
    midindex = int(rightedgeindex/2)
    mid = input_list[midindex]
    if mid == number:
        return index+midindex
    if size > 1:
        if number >= input_list[leftedgeindex] and number <= input_list[midindex-1]: 
            return recursearch(input_list[leftedgeindex:midindex],number,index)
        else:
            return recursearch(input_list[midindex+1:rightedgeindex+1],number,index + midindex + 1)
    else:
        return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[33,45,44,56,102,1,4,6,8,9,10,11,14], 10])
test_function([[33,45,44,56,102,1,4,6,8,9,10,11,14], -1])
#Add boundary null, 1 element