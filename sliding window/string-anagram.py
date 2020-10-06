""" ----------String Anagrams (hard)----------
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
1. abc
2. acb
3. bac
4. bca
5. cab
6. cba
>>> Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc". """
# NOTE: Time complexity => O(N + M) => for N and M are the number of characters in to traverse through for the 'string' and 'pattern'
# NOTE: Space complexity => O(M) => where M is the number of unique characters of 'pattern'

# --------------------------------------LOGIC STEPS---------------------------------------
# TODO: find the permutations of the pattern in the string
# TODO: need the starting index of each of the pattern permutations in the string
# -  store count of all characters in pattern in a dictionary
# - loop thru string
# - check if char from the right side (end side of window) is in hashmap 
#       -> if true: decrement count from hashmap for that character
#       -> Then check if if that char in the hashmap is equal to 0
#               -> if true: increment matched count
# - Check if matched is the same value as the length of the hashmap
#       -> if true: add the position of left character of the current window 
# - If at this point the window size is the length of the pattern, start to shrink window size:
#       -> get the char at the left side of the window & slide window by increasing the window start value
#       -> check the charater at the left end of the window is in the hashmap:
#               -> if true: then check if the value for that character in the hashmap is equal to 0
#                        -> if true: decrement matched value && add increment char count hashmap
# ----------------------------------------------------------------------------------------

def find_string_anagrams(string, pattern):
    return_indexes = []
    char_frequency = {}
    matched = 0
    window_starting = 0

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    for window_end in range(len(string)):
        right_char = string[window_end]

        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return_indexes.append(window_starting)

        if (window_end) >= len(pattern) - 1:
            left_char = string[window_starting]
            window_starting += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return return_indexes


if __name__ == "__main__":
    string_test = "ppqp"
    pattern = "pq"
    print(find_string_anagrams(string_test, pattern)) # expected output => [1, 2]
    string_test = "abbcabc"
    pattern = "abc"
    print(find_string_anagrams(string_test, pattern)) # expected output => [2, 3, 4]