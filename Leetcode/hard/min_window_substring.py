""" ------- Minimum Window Substring -------
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
>>> If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
*** A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string. """


def minWindow(s, t):
    min_length = len(s) + 1
    window_start = 0
    substring_start = 0
    matched = 0
    t_frequency_map = {}

    for char in t:
        if char not in t_frequency_map:
            t_frequency_map[char] = 0
        t_frequency_map[char] += 1
    
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in t_frequency_map:
            t_frequency_map[right_char] -= 1
            if t_frequency_map[right_char] >= 0:
                matched += 1
        # make window smaller if all characters in t have been found
        while matched == len(t):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substring_start = window_start
            
            left_char = s[window_start]
            window_start += 1

            if left_char in t_frequency_map:
                if t_frequency_map[left_char] == 0:
                    matched -= 1
                t_frequency_map[left_char] += 1
    
    if min_length > len(s):
        return ""
    return s[substring_start:substring_start + min_length]

s, t = "ADOBECODEBANC", "ABC"
print(minWindow(s, t)) # expected: "BANC"

s, t = "a", "a"
print(minWindow(s, t)) # expected: "a"

s, t = "a", "aa"
print(minWindow(s, t)) # expected: ""