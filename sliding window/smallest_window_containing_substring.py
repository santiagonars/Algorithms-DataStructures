""" ----------Problem Challenge 3----------> 
>>> ------Smallest Window containing Substring (hard)------
Given a string and a pattern, 
find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:|
Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".

Example 3:
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern. """
# NOTE: Time complexity => O(N + M) => where N and M are the number of characters in 'string' and 'pattern'
# NOTE: Space complexity => O(M) => worse case scenario for the number of unique characters in 'pattern'
#                           O(N) => worse case scenario for the output substring

def find_substring(string, pattern):
    min_length = len(string) + 1
    matched =  0
    window_start, substr_start = 0, 0
    char_frequency = {}

    # store all characters of 'pattern in a dictionary
    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0      
        char_frequency[char] += 1

    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:
                matched += 1   
        # make window smaller until a matched character is removed from the sliding window
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start # keep record of first index of the substring

            left_char = string[window_start]
            window_start += 1
            
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(string):
        return ""
    return string[substr_start:substr_start + min_length]


if __name__ == "__main__":
    string_test = "aabdec"
    pattern = "abc"
    print("Smallest substring: ", find_substring(string_test, pattern)) # expected output = "abdec"
    string_test = "abdbca"
    pattern = "abc"
    print("Smallest substring: ", find_substring(string_test, pattern)) # expected output = "bca"
    string_test = "adcad"
    pattern = "abc"
    print("Smallest substring: ", find_substring(string_test, pattern)) # expected output = ""
