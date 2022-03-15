""" ----------Rotate Array----------
Problem Statement:
>>> Given an array, rotate the array to the right by k steps, where k is non-negative.

~Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

~Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100] """

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    if k == 0 or len(nums) - k == 0:
        pass
    elif len(nums) - k > 0: 
        nums[:] = nums[-k:] + nums[:-k]
        
    elif len(nums) - k < 0:    # 7 - 8 = -1
        k_new = abs(k % len(nums))
        nums[:] = nums[-k_new:] + nums[:-k_new]
    print(nums)


if __name__ == "__main__":
    nums, k = [1, 2, 3, 4, 5, 6, 7], 3
    rotate(nums, k)