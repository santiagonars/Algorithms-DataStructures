""" ----------Ceiling of a Number (medium)----------
Problem Statement #
>>> Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. 
The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

*** Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Example 1:
Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

Example 2:
Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.

Example 3:
Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.

Example 4:
Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.
 """
# NOTE: Time complexity => O(logN) ,since we are reducing search range by half in every step, where 'N' is total number of elements in array.
# NOTE: Time complexity => O(1)


def search_ceiling_of_a_number(arr, key):
    n = len(arr)
    if key > arr[n - 1]: # no ceiling
        return -1
        
    start, end = 0, n - 1
    while start <= end:
        middle = start + (end - start) // 2
        if key < arr[middle]:
            end = middle - 1
        elif key > arr[middle]:
            start = middle + 1
        else: # found key
            return middle

    # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
    # we are not able to find the element in the given array, so the next big number will be arr[start]     
    return start


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6)) # expected output = 1
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12)) # expected output = 4
    print(search_ceiling_of_a_number([4, 6, 10], 17)) # expected output = -1
    print(search_ceiling_of_a_number([4, 6, 10], -1)) # expected output = 0


main()

