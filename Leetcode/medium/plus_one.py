""" ------- Plus One -------
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

>>> Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]t
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits does not contain any leading 0's. """


def plusOne(digits):
    tempStr = ''.join(map(str, digits)) # convert to string and concatenate
    tempStr = str(int(tempStr) + 1) # convert to interger, then add 1
    result = list(map(int, tempStr)) # convert number integer to list array of integers
    return result
    # Time: O(N)
    # Space: O(N) to store the result
 
digits = [1,2,3]
print(plusOne(digits)) # expected = [1,2,4]

digits = [4,3,2,1]
print(plusOne(digits)) # expected = [[4,3,2,2]

digits = [9]
print(plusOne(digits)) # expected = [1,0]


# ALTERNATIVE APPROACH
def plusOne_2(digits):
    num = 0
    for i in digits:
        num = num * 10 + i # i=1, num= 1 ; i=2, num= 12 ; i=3, num = 123
    num += 1
    result = list(map(int, str(num)))
    return result

""" digits = [1,2,3]
print(plusOne_2(digits)) # expected = [1,2,4]

digits = [4,3,2,1]
print(plusOne_2(digits)) # expected = [[4,3,2,2]

digits = [9]
print(plusOne_2(digits)) # expected = [1,0] """
