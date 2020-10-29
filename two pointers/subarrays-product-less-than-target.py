""" ----------Subarrays with Product Less than a Target (medium)----------
Problem Statement #
>>> Given an array with positive numbers and a target number, 
find all of its contiguous subarrays whose product is less than the target number.

Example 1:
Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Example 2:
Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target. """
# NOTE: Time complexity => O(N^3) => the main for-loop managing the sliding window takes O(N)
#                       => but creating subarrays can take up to O(N^2)
#                       => Therefore overall, the algorithm will take O(N^3) 
# NOTE: Space complexity => O(N) => ignoring the space required for the output list, 
#                        => the algorithm runs in O(N) space which is used for the temp list.
#                        -> SPACE with output list: O(N^2)

# deque: for cases where we need quicker append and pop operations from both the ends of container
from collections import deque # Doubly Ended Queue


def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right] # same as =>  product = product * arr[right]
        while (product >= target and left < len(arr)):
            product /= arr[left] # same as =>  product = product / arr[left]
            left += 1
        
        temp_list = deque()
        for i in range(right, left-1, -1): # from positive to negative; left starts at -1 bc it's exclusive
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))

    return result


def main():
    # expected output = [[2], [5], [2, 5], [3], [5, 3], [10]]
    print(find_subarrays([2, 5, 3, 10], 30)) 
    # expected output = [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]
    print(find_subarrays([8, 2, 6, 5], 50)) 


main()
