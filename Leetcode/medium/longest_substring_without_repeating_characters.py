""" ----------Longest Substring Without Repeating Characters----------
>>> Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0 

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces. """
# NOTE: Time complexity => O(N) for the first solution, O(N + N) for the second solution which is the same as O(2N)
# NOTE: Space complexity => O(K) , where K is the number of unique characters (for the size of the hashmap)


def find_longest_substring(s):
    window_start = 0
    max_length = 0
    char_index_map = {}

    # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)
        # store location of character so when it comes up  we will know where it was previously, 
        # which will be the new start of the window
        char_index_map[right_char] = window_end

        max_length = max(max_length, window_end - window_start + 1)
    return max_length

# alternative solution: 
def find_longest_substring1(s):
    max_length = 0
    window_start = 0
    char_frequency_hashmap = {}

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char not in char_frequency_hashmap:
            char_frequency_hashmap[right_char] = 0
        char_frequency_hashmap[right_char] += 1

        while char_frequency_hashmap[right_char] > 1:
            left_char = s[window_start]
            char_frequency_hashmap[left_char] -= 1
            if char_frequency_hashmap[left_char] == 0:
                del char_frequency_hashmap[left_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


# def find_longest_substring(s):
#     window_start = 0
#     max_length = 0
#     freq_char_map = {}

#     for window_end in range(len(s)):
#         char_right = s[window_end]

#         if char_right not in freq_char_map:
#             freq_char_map[char_right] = 0
#         freq_char_map[char_right] += 1

#         k = 1 # distict characters
#         while freq_char_map[char_right] > k:
#             left_char = s[window_start]
#             freq_char_map[left_char] -= 1 
#             if freq_char_map[left_char] == 0:
#                 del freq_char_map[left_char]
#             window_start += 1

#         max_length = max(max_length, window_end - window_start + 1)
#     return max_length


def main():
    s = "abcabcbb"
    print(find_longest_substring(s)) # expected output = 3
    s = "bbbbb"
    print(find_longest_substring(s)) # expected output = 1
    s = "pwwkew"
    print(find_longest_substring(s)) # expected output = 3
    s = ""
    print(find_longest_substring(s)) # expected output = 0


main()