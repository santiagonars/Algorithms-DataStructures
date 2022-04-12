""" ------- Longest Substring with At Most Two Distinct Characters -------
Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 
Constraints:
    1 <= s.length <= 105
    s consists of English letters. """


def longestSubtringWithDistictCharacters(s):
    max_length = 0
    window_start = 0
    char_frequency_map = {}

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char not in char_frequency_map:
            char_frequency_map[right_char] = 0
        char_frequency_map[right_char] += 1

        k = 2 # max number of distict characters
        while len(char_frequency_map) > k:
            left_char = s[window_start]
            char_frequency_map[left_char] -= 1
            if char_frequency_map[left_char] == 0:
                del char_frequency_map[left_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length
    # Time: O(N)
    # Space: O(K) for store at most the number of distinct elements, K, plus 1

print(longestSubtringWithDistictCharacters("eceba")) # expected = 3

print(longestSubtringWithDistictCharacters("ccaabbb")) # expected = 5
