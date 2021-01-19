""" ----------Letter Combinations of a Phone Number----------
Problem:
>>> Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. Return the answer in any order.

*** A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 
Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9']. """

from string import ascii_lowercase as alphaNums
from collections import defaultdict

# Time complexity => O(3^N * 4^M) ,where N + M is the total number of digits in the imput.
#                               => N is the number of digits in the input that maps to 3 letters (2, 3, 4, 5, 6, 8)
#                               => M is the number of digits in the input that maps to 4 letters (7, 9)
# Space complexity => O(3^N * 4^M) , as there are these many soplutions

def letter_combinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    # phone_map = {'2': ['a', 'b', 'c'],
    #              '3': ['d', 'e', 'f'],
    #              '4': ['g', 'h', 'i'],
    #              '5': ['j', 'k', 'l'],
    #              '6': ['m', 'n', 'o'],
    #              '7': ['p', 'q', 'r', 's'],
    #              '8': ['t', 'u', 'v'],
    #              '9': ['w', 'x', 'y', 'z']}
    phone_map = defaultdict(list)
    number, letters_per_num = 2, 0
    for i in range(len(alphaNums)):
        phone_map[str(number)].append(alphaNums[i])
        letters_per_num += 1

        if letters_per_num >= 3:
            if alphaNums[i] == 'r' or alphaNums[i] == 'y':
                continue
            else:
                number += 1
                letters_per_num = 0
    
    output = []
    if digits:
        backtrack("", digits, phone_map, output)
    return output


def backtrack(combination, next_digits, phone_map, output):
        if len(next_digits) == 0: # no more digits to check
            # the combination is done
            output.append(combination)
        else: # the are still digits to check
            # iterate over all the letters which map the next available digit
            for letter in phone_map[next_digits[0]]:
                # append current letter to combination and proceed to the next digit
                backtrack(combination + letter, next_digits[1:], phone_map, output)


def main():
    digits = "23"
    print(letter_combinations(digits)) # expect = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    digits = ""
    print(letter_combinations(digits)) # expect = []
    digits = "2"
    print(letter_combinations(digits)) # expect = ["a","b","c"]


main()


# alternative approach to get the letters in a phone given the digits
def get_letters(digits):
    for i in range(len(digits)):
        d = int(digits[i])
        # letter count per number
        if d == 7 or d == 9:
            letters_per_num = 4
        else:
            letters_per_num = 3
    
        if d > 7 and d <= 9:
            c2 = (int(d - 2) * 3) + 1 # if d > 7 or d <= 9
            print(alphaNums[c2], c2)
        else:
            c1 = (int(d - 2) * 3) # d <= 7; if d is equal 7 then it could be 4 letter combinations, else it is 3 letter combination for 2-6
            print(alphaNums[c1], c1)
