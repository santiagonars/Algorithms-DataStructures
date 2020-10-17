""" ----------Problem Statement---------- 
>>> --------Pair with Target Sum (easy)---------
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11 """
# NOTE: Time complexity - APPROACH 1) => O(N) =>  N is the total number of elements in the array
#                       - APPROACH 2) => O(N) => N is the total number of elements in the array
# NOTE: Space complexity - APPROACH 1) => O(1) => only need to store 2 index locations of the array
#                        - APPROACH 2) => O(N) => as worse case because nums can be as big as the array

def pair_with_targetsum1(arr, target_sum):
    left, right = 0, len(arr) - 1 # point to the index at each end of the array
    while (left < right):
        current_sum = arr[left] + arr[right]
        # check if the sum of the 2 values currently pointed at is equal to the 'target_sum'
        if current_sum == target_sum:
            return [left, right]
        # if the 'current_sum' is greater than the target, we need to decrease the sum by decreasing right pointer index
        if current_sum > target_sum:
            right -= 1
        # if the 'current_sum' is less than the target, we need to increase the sum by increasing the left pointer index
        if current_sum < target_sum:
            left += 1
    return [-1, -1]

# ALTERNATIVE approach using a HASHMAP
"""  # Search for ‘Y’ (which is equivalent to “Target - X”) in the HashTable. 
    # -> If it is there, we have found the required pair.
    # Otherwise, insert “X” in the HashTable, so that we can search it for the later numbers. """
def pair_with_targetsum2(arr, target_sum):
    nums = {} # dict to track numbers and in their indices
    for i, num in enumerate(arr):
        if (target_sum - num) in nums:
            return [nums[target_sum - num], i]
        else:
            nums[num] = i  # OR -> nums[arr[i]] = i
    return [-1, -1]


if __name__ == "__main__":
    # APPROACH 1
    array_test = [1, 2, 3, 4, 6]
    target = 6
    print(pair_with_targetsum1(array_test, target)) # expected output = [1, 3]
    array_test = [2, 5, 9, 11]
    target = 11
    print(pair_with_targetsum1(array_test, target))  # expected output = [0, 2]
    # APPROACH 2
    array_test = [1, 2, 3, 4, 6]
    target = 6
    print(pair_with_targetsum2(array_test, target)) # expected output = [1, 3]
    array_test = [2, 5, 9, 11]
    target = 11
    print(pair_with_targetsum2(array_test, target))  # expected output = [0, 2]