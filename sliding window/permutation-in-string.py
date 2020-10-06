""" ----------Permutation in a String (hard)----------
Given a string and a pattern, find out if the string contains any permutation of the pattern.
<<<Permutation>>> is defined as the re-arranging of the characters of the string. 
For example, “abc” has the following six permutations:
1. abc
2. acb
3. bac
4. bca
5. cab
6. cba
*******>>>> If a string has ‘n’ distinct characters it will have n! permutations.

Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern. """
# NOTE: Time complexity => 
# NOTE: Space complexity =>
from math import factorial

def find_permutation(string, pattern):
    # print(factorial(len(pattern))) # number of permutations in 'pattern'
    window_start = 0
    matched = 0
    char_frequency = {}

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
    
    for window_end in range(len(string)):
        right_char = string[window_end]
        # try matching all characters from 'char_frequency' in all characters in current window
        if right_char in char_frequency:
            # decrease the frequency count of the character that matched
            char_frequency[right_char] -= 1   
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True
            
        # start sliding window once it matches the size of the pattern
        if window_end >= len(pattern) - 1:
            left_char = string[window_start]
            window_start += 1
            # check if character that is going to leave window was present in 'char_frequency'
            if left_char in char_frequency:
                # if the value of a character in 'char_frequency' is equal to 0, and matched was increase, we need to decrease it again.
                if char_frequency[left_char] == 0:
                    matched -= 1
                # account of character that is about to leave window back in 'char_frequency'
                char_frequency[left_char] += 1
    return False


if __name__ == "__main__":
    string_test = "oidbcaf"
    pattern = "abc"
    print("Contains permutation: ", find_permutation(string_test, pattern)) # expected output = true
    string_test = "odicf"
    pattern = "dc"
    print("Contains permutation: ", find_permutation(string_test, pattern)) # expected output = false
    string_test = "bcdxabcdy"
    pattern = 'bcdyabcdx'
    print("Contains permutation: ", find_permutation(string_test, pattern)) # expected output = true
    string_test = "aaacb"
    pattern = "abc"
    print("Contains permutation: ", find_permutation(string_test, pattern)) # expected output = true