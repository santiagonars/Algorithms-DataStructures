""" ----------Minimum Window Substring----------
Problem:
>>> Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".

***Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Constraints:
    1 <= s.length, t.length <= 105
    s and t consist of English letters.

Follow up: Could you find an algorithm that runs in O(n) time? """

"""
PLANNING (psedo/notes):
if t is empty: return ""
add t in dictionary (hashmap)
count = 0
minLenWindow = ""
window_start = 0
for window_end in len(s):
    if char in t_dict:
        t_dict[char] -= 1
        count += 1

    if count == len(t):
        t_dict[t[window_start] ] += 1 
        window_start += 1
        count -=1
        if len(minLenWindow) < len(t[window_start, window_end + 1])
            minLenWindow = t[window_start, window_end + 1]

return 
"""

def findMinWindow(s, t):
    if len(t) == 0:
        return ""

    t_dict = {}
    window_start = 0
    count = 0
    minWindow = s
    
    for window_end in s:
        if window_end in t_dict:
            if t_dict[window_end] == 0:
                del t_dict[window_end]
            t_dict -= 1
            count += 1
    
        if count == len(t):
            if len(minWindow) < t[window_start:window_end+1]:
                minWindow = t[window_start:window_end+1]
            
            if t_dict[window_start] == 0:
                t_dict[window_start] = 1
            else:
                t_dict[window_start] += 1
            window_start += 1
    
    if len(minWindow) == len(s):
        return ""
    
    return minWindow

def main():
    s, t = "ADOBECODEBANC", "ABC"
    print(findMinWindow(s, t)) # expect = "BANC"

    # s, t = "a", "a"
    # print(findMinWindow(s, t)) # expect = "a"

main()