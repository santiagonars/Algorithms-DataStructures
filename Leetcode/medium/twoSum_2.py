""" --------Two Sum II - Input Array Is Sorted------
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

>>> Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2]. """


def twoSum(numbers, target):
    low = 0
    high = len(numbers)-1

    while low < high:
        if numbers[low] + numbers[high] == target:
            return [low+1, high+1]
        elif numbers[low] + numbers[high] < target:
            low += 1
        else:
            high -= 1
    # Time: O(N)
    # Space: O(1) -> constant space


# PROBLEM: This solution doesn't use constant space; since it's sorted it should make use of that
def twoSum_2(numbers, target): 
    comp_map = {} # index map for complement
    
    for i in range(len(numbers)):
        complement = target - numbers[i]
        
        if complement in comp_map:
            return [comp_map[complement] + 1, i + 1]
        else:
            comp_map[numbers[i]] = i 
    # Time: O(N)
    # Space: O(N)

numbers, target = [2,7,11,15], 9 # expected output = [1,2]
print(twoSum(numbers, target))

numbers, target = [2,3,4], 6 # expected output = [1,3]
print(twoSum(numbers, target))

numbers, target = [-1,0], -1 # expected output = [1,2]
print(twoSum(numbers, target))