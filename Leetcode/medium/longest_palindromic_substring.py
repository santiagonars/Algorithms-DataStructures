""" ----------Longest Palindromic Substring (Medium)----------
Problem:
>>> Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a" """
# Time complexity => O(N^2) 
# Space complexity => O(1)

# Solution by 'expanding around the center'
def longestPalindrome(s):
    maxlen = 0
    start = 0

    for i in range(len(s)):
        maxlen, start = expandFromCenter(s, i, i, maxlen, start) # covers case #1 (odd) -> "racecar"
        maxlen, start = expandFromCenter(s, i, i+1, maxlen, start) # covers case #2 (even) -> "aabbaa"
    return s[start:start+maxlen]


def expandFromCenter(s, left, right, maxlen, start):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1 
        right += 1 

    if maxlen < right - left - 1:
        maxlen = right - left - 1 
        start = left + 1  
    
    return maxlen, start

def main():
    s = "babad"
    print(longestPalindrome(s)) # expected = "bab"
    s = "cbbd"
    print(longestPalindrome(s)) # expected = "bb"
    s = "a"
    print(longestPalindrome(s)) # expected = "a"  # NOTE: A single character is considered a palindrome!
    s = "ac"
    print(longestPalindrome(s)) # expected = "a"
    


main()
