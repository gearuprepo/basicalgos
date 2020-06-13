# Search in a Rotated Sorted Array
The algo recursively compares the pivot with left half and right half and based on the comparison, it works on either left half or right half. 

The number is found out by halving the inputlist arriving at a runtime of logn. 

time O(n) = log n
space O(n) = log n

Eg. Stack trace
recursearch([[6, 7, 8, 1, 2, 3, 4], 8])
 - recursearch([[6, 7, 8], 8])
     - recursearch([[7, 8], 8])
         - recursearch([[8], 8])

Review comment fixes:
1. Fixed code for edge cases.