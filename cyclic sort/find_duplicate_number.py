""" ----------Find the Duplicate Number (easy)----------
Problem Statement #
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 
>>> Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:
Input: [1, 4, 4, 3, 2]
Output: 4

Example 2:
Input: [2, 1, 3, 3, 5, 4]
Output: 3

Example 3:
Input: [2, 4, 1, 4, 4]
Output: 4 """
# NOTE: Time complexity => 
# NOTE: Space complexity =>


def find_duplicate_number(nums):
    i = 0

    while i < len(nums):
        # check if number is in the correct location
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i] # there is only one duplicate
        else:
            i += 1
    return []


def main():
    print(find_duplicate_number([1, 4, 4, 3, 2])) # expected output = 4
    print(find_duplicate_number([2, 1, 3, 3, 5, 4])) # expected output = 3
    print(find_duplicate_number([2, 4, 1, 4, 4])) # expected output = 4


main()

# NOTE: The is only ONE DUPLICATE! 
# - if while swapping the number with its index both the numbers being swapped are same, we have found the duplicate!

