""" -----3Sum-----
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

>>> Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
"""

def threeSum(nums):
    # if len(nums) < 3:
    #     return []
    triplets = []
    target = 0
    triplet_frequency_map = {}
    nums.sort()
    for i in range(len(nums) - 2):
        comp_map = {}
        for j in range(i + 1, len(nums)):
            complement = target - nums[i] - nums[j]
            if complement in comp_map:
                if (nums[i], nums[comp_map[complement]], nums[j]) not in triplet_frequency_map:
                    triplet_frequency_map[( nums[i], nums[comp_map[complement]], nums[j] )] = 0
                triplet_frequency_map[(nums[i], nums[comp_map[complement]], nums[j])] += 1

                if triplet_frequency_map[(nums[i], nums[comp_map[complement]], nums[j])] <= 1:
                    triplets.append([ nums[i], nums[comp_map[complement]], nums[j] ])
            else:
                comp_map[nums[j]] = j      

    return triplets
    # Time: O(N ^ 2)
    # Space: O(2N)


nums = [-1,0,1,2,-1,-4] # expected: [[-1,-1,2],[-1,0,1]]
result = threeSum(nums)
print(result)

nums = [] # expected: []
result = threeSum(nums)
print(result)

nums = [0] # expected: []
result = threeSum(nums)
print(result)