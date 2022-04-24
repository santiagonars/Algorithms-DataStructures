""" ------- Backspace String Compare -------
Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
>>> '#' means a backspace character. (Meaning it deletes the previous one character)

>>> Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.
 
>>> Follow up: Can you solve it in O(n) time and O(1) space? """


""" ----- SOLUTION: Build string ----- """
# def backspaceCompare(s, t):
#     def build(input_string):
#         res = []
#         for char in input_string:
#             if char != '#':
#                 res.append(char)
#             elif res:
#                 res.pop()
#         return "".join(res)
#     return build(s) == build(t)
#     # Time: O(M + N)  where N, M are the lengths of s and t respectively
#     # Space: O(N)

""" ----- SOLUTION: Two Pointers ----- """
from itertools import zip_longest
def backspaceCompare(s, t):
    def func(str):
        skip = 0
        for c in reversed(str):
            if c == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield c
    return all(x == y for x, y in zip_longest(func(s), func(t)))
    # Time: O(N)
    # Space: O(1)

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t)) # expected output = true

s = "ab##"
t = "c#d#"
print(backspaceCompare(s, t)) # expected output = true

s = "a#c"
t = "b"
print(backspaceCompare(s, t)) # expected output = false