""" ----------Order-agnostic Binary Search (easy)----------
Problem Statement #
>>> Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
You should assume that the array can have duplicates.

*** Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

NOTE: -> ORDER 'AGNOSTIC' means that we don't know if order is ascending or descending.
NOTE: No integer overflow problem in Python, only in Java or C++

Example 1:
Input: [4, 6, 10], key = 10
Output: 2

Example 2:
Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4

Example 3:
Input: [10, 6, 4], key = 10
Output: 0

Example 4:
Input: [10, 6, 4], key = 4
Output: 2 """
# NOTE: Time complexity => O(logN) ,since we are reducing search range by half in every step, where 'N' is total number of elements in array.
# NOTE: Time complexity => O(1), since we're only storing index values.


def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    isAscending = arr[start] < arr[end]
    
    while start <= end:
         # calculate the middle of the current range
        # middle = int((start + end) / 2)
        middle = start + (end - start) // 2

        if key == arr[middle]:
            return middle

        if isAscending: # ascending order
            if key < arr[middle]:
                end = middle - 1  # the 'key' can be in the first half
            else: # key > arr[middle]
                start = middle + 1 # the 'key' can be in the second half
        else: # descending order
            if key > arr[middle]:   
                end = middle - 1  # the 'key' can be in the first half
            else: # key < arr[middle]
                start = middle + 1  # the 'key' can be in the second half
    
    return -1


def main():
    print(binary_search([4, 6, 10], 10)) # expected output = 2
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5)) # expected output = 4
    print(binary_search([10, 6, 4], 10)) # expected output = 0
    print(binary_search([10, 6, 4], 4)) # expected output = 2


main()


# NOTE: -----Steps for Binary Search (ASCENDING):-----
#   1.) Let’s assume start is pointing to the first index and end is pointing to the last index of the input array 
#        (let’s call it arr). This means:
# 
#              int start = 0;
#              int end = arr.length - 1;
# 
#   2.) SKIP THIS STEP IN PYTHON => there is no integer overflow problem in pure Python.
#       First, we will find the middle of start and end. An easy way to find the middle would be:
#          middle=(start+end)/2. For Java and C++, this equation will work for most cases, but when start or end is large, 
#          this equation will give us the wrong result due to integer overflow. 
#          Imagine that end is equal to the maximum range of an integer (e.g. for Java: int end = Integer.MAX_VALUE). 
#          Now adding any positive number to end will result in an integer overflow. 
#          Since we need to add both the numbers first to evaluate our equation, an overflow might occur. 
#          The safest way to find the middle of two numbers without getting an overflow is as follows:
# 
#               middle  = start + (end-start)/2
# 
#   3.) Next, we will see if the ‘key’ is equal to the number at index middle. 
#       If it is equal we return middle as the required index.
# 
#   4.) If ‘key’ is not equal to number at index middle, we have to check two things:
#        -> If key < arr[middle], then we can conclude that the key will be smaller than all the numbers after index middle 
#            as the array is sorted in the ascending order. Hence, we can reduce our search to end = mid - 1.
#        -> If key > arr[middle], then we can conclude that the key will be greater than all numbers before index middle 
#            as the array is sorted in the ascending order. Hence, we can reduce our search to start = mid + 1.
# 
#   5.) We will repeat steps 2-4 with new ranges of start to end. If at any time start becomes greater than end, 
#       this means that we can’t find the ‘key’ in the input array and we must return ‘-1’.

# -------For DESCENDING order, amke there changes:-------
#    - If key > arr[middle], then we can conclude that the key will be greater than all numbers 
#       after index middle as the array is sorted in the descending order. 
#       Hence, we can reduce our search to end = mid - 1.
#    - If key < arr[middle], then we can conclude that the key will be smaller than all the numbers 
#       before index middle as the array is sorted in the descending order. 
#       Hence, we can reduce our search to start = mid + 1.

# *** Finally, how can we figure out the sort order of the input array? 
# >>> We can compare the numbers pointed out by start and end index to find the sort order <<<
#     If arr[start] < arr[end]:
#       it means that the numbers are sorted in ascending order otherwise they are sorted in the descending order.