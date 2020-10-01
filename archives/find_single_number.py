# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#  ->  Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# ----------------------------------------------------------------------------------------------------------------
from collections import defaultdict

def main():
    nums = [4,1,2,1,2]
    print(nums)
    print(singleNumber(nums))

    nums = [2,2,1]
    print(nums)
    print(singleNumber(nums))

def singleNumber(nums):
    # using an default initized dictionary -> fastest
    '''hash_table = defaultdict(int) # values are defaulted to be initized with an integer value

    for i in nums:
        hash_table[i] += 1
        
    for i in hash_table:
        if hash_table[i] == 1:
            return i'''
        
    # using a regular ditionary -> 2nd fastest
    hash_table = dict()

    for i in nums:
        if i in hash_table.keys():
            hash_table[i] += 1
        else:
            hash_table[i] = 1 # need to initize every new key 
            
    for i in hash_table:
        if hash_table[i] == 1:
            return i

    # using a regular ditionary (initilizing all values to zero first) -> 3rd fastest
    '''hash_table = dict()

    for i in nums:
        hash_table[i] = 0
        
    for i in nums:
        hash_table[i] += 1
            
    for i in hash_table:
        if hash_table[i] == 1:
            return i'''


if __name__ == "__main__":
    main()