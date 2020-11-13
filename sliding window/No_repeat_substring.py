""" ----------Problem Statement----------
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde". """
# NOTE: Time complexity => O(N) => all hashmap operations are constant
# NOTE: Space complexity => O(K) => for the size of the hashmap, where K is <= N

def non_repeat_substring(str):
    max_length = 0
    window_start = 0
    char_frequency = {} 
    # use a sliding window through 'str'
    for window_left in range(len(str)):
        # store unique characters in hashmap (dict)
        right_char = str[window_left]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        # check for repeating character
        # as long char_frequency[right_char] > 1, meaning it's repeated, remove previous character value and shrink window 
        while char_frequency[right_char] > 1:
            new_start_window = len(char_frequency)
            char_frequency.clear()
            char_frequency[right_char] = 1
            window_start += new_start_window
        # save the maximum length so far
        max_length = max(max_length, window_left - window_start + 1)
    return max_length

# Alternate algorithm
def non_repeat_substring1(str1):
    window_start = 0
    max_length = 0
    char_index_map = {}

    # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # if the map already contains the 'right_char', shrink the window from the beginning so that
        # we have only one occurrence of 'right_char'
        if right_char in char_index_map:
            # this is tricky; in the current window, we will not have any 'right_char' after its previous index
            # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
            window_start = max(window_start, char_index_map[right_char] + 1)
        # insert the 'right_char' into the map
        char_index_map[right_char] = window_end
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == "__main__":
    string_test1 = "aabccbb"
    print("Length of the longest substring: ", non_repeat_substring(string_test1)) # expected output = 3
    string_test2 = "abbbb"
    print("Length of the longest substring: ", non_repeat_substring(string_test2)) # expected output = 2
    string_test3 = "abccde"
    print("Length of the longest substring1: ", non_repeat_substring(string_test3)) # expected output = 3

    string_test1 = "aabccbb"
    print("Length of the longest substring (ALT): ", non_repeat_substring1(string_test1)) # expected output = 3
    string_test2 = "abbbb"
    print("Length of the longest substring (ALT): ", non_repeat_substring1(string_test2)) # expected output = 2
    string_test3 = "abccde"
    print("Length of the longest substring (ALT): ", non_repeat_substring1(string_test3)) # expected output = 3
