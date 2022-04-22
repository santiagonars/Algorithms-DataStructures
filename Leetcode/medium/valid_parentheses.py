""" ------- Valid Parenthesis -------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
>>> determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 
Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
 """

# Use a stack
def isValid(s):
    char_mapping = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
        if char in char_mapping:
            
            item = stack.pop() if stack else 'd'

            if item != char_mapping[char]:
                return False
        else:
            stack.append(char)
    return stack == [] #  can also use `not stack`
    # Time: O(N)
    # Space: O(N)


s = "()"
print(isValid(s)) # expected output = true

s = "()[]{}" 
print(isValid(s)) # expected output = true

s = "(]"
print(isValid(s)) # expected output = false