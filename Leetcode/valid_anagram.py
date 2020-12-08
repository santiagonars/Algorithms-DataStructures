""" ----------Valid Anagram----------
PROBLEM:
>>> Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
*** You may assume the string contains only lowercase alphabets.

Follow up:
> What if the inputs contain unicode characters? How would you adapt your solution to such case """
# Time complexity => O(N) ,to traverse all characters in 's'
# Space complexity => O(1) ,because it only contains alphabet characters


import collections

# Solution #1: faster execution 
def isAnagram(s, t):
    return collections.Counter(s) == collections.Counter(t)


# Solution #2: iteration
""" 
NOTE(S): ALGORITHM STEPS
add 't' in a frequecy hashmap
for loop every character in s
    if char is in 't': remove char from hashmap
    else: return false
if length of hashmap is not equal to 0: return false
return true; since now we know that all characters in t are present in s
> time complexity: O(N)
> space complexity: O(M)
"""
def isAnagram_2(s, t):
    """ 
    :type s: str
    :type t: str
    :rtype: bool
    """
    frequency_map = collections.Counter(t)

    for char in s:
        # if char present in 's' is also in 't'
        if char in frequency_map:
            frequency_map[char] -= 1
            if frequency_map[char] == 0:
                del frequency_map[char]
        else:
            return False

    # 't' has more characters than 's'
    if len(frequency_map) != 0:
        return False

    # all characters in 't' are present in 's'
    return True

# Solution #1
s, t = "anagram", "nagaram"
print(isAnagram(s, t))
s, t = "rat", "car"
print(isAnagram(s, t))
# Solution #2
s, t = "anagram", "nagaram"
print(isAnagram_2(s, t))
s, t = "rat", "car"
print(isAnagram_2(s, t))