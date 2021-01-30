""" ----------Move Zeroes----------
Problem:
>>> Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations. """


""" 
>>> Agorithm:
for loop every number in array:
    while number is zero, swap with next possible non-zero number
>>> alternative: keep track of the last non-zero index
 """
# Time complexity: O(N), worse case O(N + N) where all numbers are zeros
# Space complexity: O(1)
def moveZeroes(nums):
    n = len(nums)
    count = 0
    i = 0
    while i < n:
        j = 0
        while nums[i] == 0 and i + 1 + j < n:
            nums[i], nums[i + 1 + j] = nums[i + 1 + j], nums[i]
            j += 1
            print(nums)
        i += 1
    # print(nums)


def main():
    nums = [0,1,0,3,12]
    moveZeroes(nums) # expect = [1,3,12,0,0]


main()