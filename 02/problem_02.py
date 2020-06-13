# Search in a Rotated Sorted Array
#O(n) = log n
def rotated_array_search(input_list, number):
    if len(input_list) == 0:
        raise Exception("Invalid input array") 
    retval = recursearch(input_list,number,0)
    return retval


def recursearch(input_list,number,index):
    size = len(input_list)
    rightedgeindex = size - 1
    leftedgeindex = 0
    midindex = int(rightedgeindex/2)
    mid = input_list[midindex]
    left = input_list[leftedgeindex]
    right = input_list[rightedgeindex]
    if mid == number:
        return index+midindex
    if size > 1:
        if left <= mid:
            if number >= left and number <= mid: 
                return recursearch(input_list[leftedgeindex:midindex],number,index)
            else:
                return recursearch(input_list[midindex+1:rightedgeindex+1],number,index + midindex + 1)
        #Fix for Edge cases
        if number > mid and number < right:
             return recursearch(input_list[midindex+1:rightedgeindex+1],number,index + midindex + 1)
        else:
            return recursearch(input_list[leftedgeindex:midindex],number,index)
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

#egde test 2  large list
test_list=[i for i in range (1011,10000)]+[i for i in range (0,1011)]
test_function([test_list, 0])
#egde test 3  large list with negative numbers
test_list=[i for i in range (1011,10000)]+[i for i in range (-1000,1011)]
test_function([test_list, -60])
#egde test 1  empyt string
test_function([[], 1])