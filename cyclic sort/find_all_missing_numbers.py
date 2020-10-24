""" ----------Find all Missing Numbers (easy)----------
Problem Statement #
>>> We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example 1:
Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Example 2:
Input: [2, 4, 1, 2]
Output: 3

Example 3:
Input: [2, 3, 2, 1]
Output: 4 """
# NOTE: Time complexity => O(N), the while loop is O(N) and the for loop is also O(N), hence O(N + N) which is same as O(N)
# NOTE: Space complexity => O(1), the actual algorithm is constant without accounting for the output array


def find_missing_numbers(nums):
    i = 0
    # this will sort the values except the missing values 
    while i < len(nums):
        j = nums[i] - 1 # value = index + 1; then check nums[value]
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i] # swap numbers
        else:
            i += 1

    missingNumbers = []

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)

    return missingNumbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1])) # expected output = 4, 6, 7
    print(find_missing_numbers([2, 4, 1, 2])) # expected output = 3
    print(find_missing_numbers([2, 3, 2, 1])) # expected output = 4


main()

# it is unsorted array
# numbers are from 1 to n
# it has duplicates which, then some of the values in 1 to n are missing; TODO => need to return array of missing values!
# # NOTE: 
# while loop as loop through 'n' elements in the array
# if index of the number is not the same as the number; swap
# if it is the same; increase i (move the next 'n' postion in the array)
# then loop through array and check any indices missing the correct numbers