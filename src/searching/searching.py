# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start = None, end= None): # O(log n)
    # Your code here
    if start is None:
        start = 0
    if end is None:
        end = len(arr)
    if start > end:
        print("nah, it's not here")
        return -1
    middle = (start+end) // 2 # this is taking the result start /2  #O (1)
    if arr[middle] == target:  # checks if the middle is the target
        return middle
    elif arr[middle] <target:
        return binary_search(arr,target, middle +1, end)
    else:
        return binary_search(arr, target, start, middle -1)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

