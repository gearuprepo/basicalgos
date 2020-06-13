# O(n) = nlogn + 2n => nlogn
def rearrange_digits(input_list):
    #Fix for boundary condition.
    if len(input_list)==0:
        raise Exception("Insufficient data")
    
    if len(input_list) == 1:
        return input_list[0],0
    arr = QuickSort(input_list) #O(n) = nlogn
    number1 = (arrtoint(arr[::2])) #O(n) = n
    number2 = (arrtoint(arr[1::2])) #O(n) = n
    return number1,number2

#O(n) = n
def arrtoint(arr):
    strings = [str(integer) for integer in arr]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer

#O(n) = nlogn
def QuickSort(arr):
    size = len(arr)
    if size < 2:
        return arr
    current_position = 0 
    for i in range(1, size): 
         if arr[i] >= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp
    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp 
    left = QuickSort(arr[0:current_position]) 
    right = QuickSort(arr[current_position+1:size])
    arr = left + [arr[current_position]] + right 
    return arr

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[1,2], [1,2]]
test_function(test_case)

test_case = [[1,2,3], [31,2]]
test_function(test_case)

test_case = [[0,1,2,3,4,5,6,7,8,9], [97531,86420]]
test_function(test_case)

test_case = [[1], [1,0]]
test_function(test_case)

