""" ----------Two Single Numbers (medium)----------
Problem Statement #
>>> In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. 
Find the two numbers that appear only once.

Example 1:
Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]

Example 2:
Input: [2, 1, 3, 2]
Output: [1, 3] """
# NOTE: Time complexity => O(N) ,where ‘n’ is the number of elements in the input array.
# NOTE: Space complexity => O(1) 


def find_single_numbers(nums):
    # get the XOR of the all the numbers
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # get the rightmost bit that is '1'
    rightmost_set_bit = 1
    #  & is the bitwise AND operator: 
    #    -> If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.
    while (rightmost_set_bit & n1xn2) == 0: 
        rightmost_set_bit = rightmost_set_bit << 1 # returns 'rightmost_set_bit' with the bits shifted to the left by 1 place
    num1, num2 = 0, 0

    # since the right most bit for one number will be 0 and the other 1, doing the bitwise AND will separate it into 2 groups
    for num in nums:
        if (num & rightmost_set_bit) != 0: # the bit is set (the bit matched and returns same as 'rightmost_set_bit')
            num1 ^= num
        else: # the bit is not set (so the bit does not so it returns all 0s)
            num2 ^= num

    return [num1, num2]


def main():
    # answer = [4, 6]
    print('Single numbers are:' + str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))) 
    # answer = [1, 3]
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2]))) 


main()


# NOTE: Solution
# ----------Explanation----------
# Let’s assume num1 and num2 are the two single numbers. If we do XOR of all elements of the given array, 
# we will be left with XOR of num1 and num2 as all other numbers will cancel each other because all of them appeared twice. 
# Let’s call this XOR n1xn2. Now that we have XOR of num1 and num2, how can we find these two single numbers?
# 
# As we know that num1 and num2 are two different numbers, therefore, they should have at least one bit different between them. 
# If a bit in n1xn2 is ‘1’, this means that num1 and num2 have different bits in that place, 
# as we know that we can get ‘1’ only when we do XOR of two different bits. Example:
# 
#         1 XOR 0 = 0 XOR 1 = 1
# 
# We can take any bit which is ‘1’ in n1xn2 and partition all numbers in the given array into two groups based on that bit. 
# One group will have all those numbers with that bit set to ‘0’ and the other with the bit set to ‘1’. 
# This will ensure that num1 will be in one group and num2 will be in the other. 
# We can take XOR of all numbers in each group separately to get num1 and num2, 
# as all other numbers in each group will cancel each other.
# 
# ----------Steps of algorithm----------
# 1) Taking XOR of all numbers in the given array will get the XOR of num1 and num2 (call this XOR as 'n1xn2').
# 2) Find any bit which is set in n1xn2. We can take the rightmost bit which is ‘1’ (call it 'rightmostSetBit').
# 3) Iterate through all numbers of the input array to partition them into two groups based on 'rightmostSetBit'. 
# 4) Take XOR of all numbers in both the groups separately. Both these XORs are the required numbers.
