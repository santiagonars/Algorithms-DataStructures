""" ----------Find the Missing Number (easy)----------
Problem Statement #
>>> We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:
Input: [4, 0, 3, 1]
Output: 2

Example 2:
Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7 """ 
# NOTE: Time complexity => O(N) . It will iterate but not increase i when swapping in the while loop up tp 'n-1'
#                       => then once at the correct index it will contunue to iterate increasing i, resulting in
#                       => this results in  O(n) + O(n-1) + O(n) which is aysmptoticaly equivalent to O(N)
# NOTE: Space complexity => O(1)

def find_missing_number(nums):
    i = 0
    n = len(nums)
    while (i < n):
        j = nums[i] # number should be equal to the index because we array starts at 0, hence nums[i] == nums[nums[i]]
        # Since the array will have ‘n’ numbers, it means array indices will range from 0 to ‘n-1’.
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    # find the first number missing from its index, that will be the required number
    for i in range(n):
        if nums[i] != i:
            return i

    return n


if __name__ == "__main__":
    print(find_missing_number([4, 0, 3, 1])) # expected output = 2
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1])) # expected output = 7
