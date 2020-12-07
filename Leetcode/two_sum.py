""" ----------Two Sum----------
Problem:
>>> Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

***You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1] 

Constraints:
    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists. """
# Time complexity => O(N) to iterate through nums
# Space complexity => O(N) to store the all the elements of num in the array

""" 
----------NOTE(S):----------
X + Y = TARGET  => Y = TARGET - X 
- add input array to a an index hashmap with elements with correspoding values
- For loop i thru entire input array:
    complement = target - array[i]
    if complement exist in hashmap: 
        return [complement, array[i]]
    else:
        hashmap[array[i]] = i
"""


def twoSum(nums, target):
    comp_map = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in comp_map:
            return [comp_map[complement], i]
        else:
            comp_map[nums[i]] = i

    # there are not 2 elements sums to equal target
    return -1 


def main():
    print(twoSum([2,7,11,15], 9)) # expected = [0,1]
    print(twoSum([3,2,4], 6)) # expected = [1,2]
    print(twoSum([3,3], 6)) # expected = [0,1]


main()