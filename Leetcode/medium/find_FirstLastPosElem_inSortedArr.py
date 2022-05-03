""" ------- Find First and Last Position of Element in Sorted Array -------

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109 """



""" ----- SOLUTION: Binary Search ----- """
class Solution:
    def searchRange(self, nums, target):
        
        lower = self.findBound(nums, target, True)
        if (lower == -1):
            return [-1, -1]
        
        upper = self.findBound(nums, target, False)
        
        return [lower, upper] 
    
    def findBound(self, nums, target, isFirst):
        n = len(nums)
        begin, end = 0, n - 1
        while begin <= end:
            mid = int((begin + end) / 2)

            if nums[mid] == target:

                if isFirst:
                    if mid == begin or nums[mid - 1] < target:
                        return mid
                    end = mid - 1
                else:
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    begin = mid + 1

            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return -1
    # Time: O(logN) using binary search
    # Space: O(1)


s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums, target)) # expect: [3,4]

nums = [5,7,7,8,8,10]
target = 6
print(s.searchRange(nums, target)) # expect: [-1,-1]

nums = []
target = 0
print(s.searchRange(nums, target)) # expect: [-1,-1]




