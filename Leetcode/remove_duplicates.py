""" ----------Problem Statement----------
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2]
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4]
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length. """
# NOTE: Time complexity => O(N) / ALTERNATIVE solution is O(N*Log(N)) but runs faster for use cases
# NOTE: Time complexity => O(N)

def removeDuplicates(nums):
    # ALTERNATE: only the 2 lines below and seems faster at first but once N is latger but it isnt 
    # Time complexity => O(N*logN) to sort the array
    # s = set(nums)
    # nums[:] = sorted(s)

    unique_values = {}
    new = []
    for window_end in range(len(nums)):
        # add uniques values from array in hashmap
        n = nums[window_end]
        if n not in unique_values:
            unique_values[n] = 0
        unique_values[n] += 1
        # save unique value for n as long as it there is more than 1 present in hashmap
        if unique_values[n] == 1:
            new.append(n)      
    nums[:] = new
    print("new nums: ", nums)
    return len(nums)

if __name__ == "__main__":
    arraytest1 = [1,1,2] 
    print(removeDuplicates(arraytest1)) # expected output = 2 | new nums = [1,2] 
    arraytest2 = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(arraytest2)) # expected output = 5 | new nums = [0,1,2,3,4]