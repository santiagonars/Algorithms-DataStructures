""" ----------First Unique Character in a String----------
Problem:
>>> Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Example 1:
s = "leetcode"
return 0.

Example 2:
s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters """
# Time complexity => O(N) => O(N + N) = O(2N) which is asymptotically equivalent to O(N)
# Space complexity => O(1) => where N can be up to 26 characters in the English alphabet

# solution #1
def firstUniqChar(s):
    freq_map = {}

    # add to characters in s to dictionary
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1

    # iterate all characters in string and check dictionary for frequency value
    for i in range(len(s)):
        char = s[i]
        if freq_map[char] == 1:
            return i
    return -1

# solution #2 -  using python built-in collections 
import collections

def firstUniqChar_2(s):

    # hashmap of how often character appears
    count = collections.Counter(s)

    # find index
    for idx, char, in enumerate(s):
        if count[char] == 1:
            return idx
    return -1

# solution #1
print(firstUniqChar("leetcode")) # expected output = 0
print(firstUniqChar("loveleetcode")) # expected output = 2
# solution #2
print(firstUniqChar_2("leetcode")) # expected output = 0
print(firstUniqChar_2("loveleetcode")) # expected output = 2