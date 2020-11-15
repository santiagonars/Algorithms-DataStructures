""" ----------Single Number (easy)----------
Problem Statement #
>>> In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:
Input: 1, 4, 2, 1, 3, 2, 3
Output: 4

Example 2:
Input: 7, 9, 7
Output: 9 """
# NOTE: Time complexity => O(N) to iterate through all numbers of the input array once.
# NOTE: Space complexity => O(1) .It is constant space as it only uses the num variable


def find_single_number(arr):
    num = 0
    for i in arr:
        num ^= i # num = num ^ i ; take the XOR or each number and uses the result to XOR with the next number, and so on.
    return num


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))


main()

# NOTE: this problem can be solved with a hashmap with an O(N) time complexity and O(N) space complexity.
# 
# Recall the following two properties of XOR:
#   - It returns zero if we take XOR of two same numbers.
#   - It returns the same number if we XOR with zero.
# 
# Using a XOR solution, we can XOR all the numbers in the input; 
# >>>>>>> duplicate numbers will zero out each other and we will be left with the single number.









