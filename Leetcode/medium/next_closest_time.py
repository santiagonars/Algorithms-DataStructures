""" ------- Next Closest Time -------
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. 
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. 
    For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:
Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:
Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

Constraints:
    time.length == 5
    time is a valid time in the form "HH:MM".
    0 <= HH < 24
    0 <= MM < 60 """


def next_closest_time(time):
    hh, mm = time.split(":")
    minutes = int(hh) * 60 
    minutes += int(mm)
    # ALTENATIVE:
    # minutes = int(time[:2]) * 60 # convert HH to minutes
    # minutes += int(time[3:]) # add MM and HH in minutes
    
    t = hh + mm
    digits_set = set(map(int, t)) # use a set to check if an object is in it
    
    while True:
        minutes = (minutes + 1) % (24 * 60) # modules operator by (40 * 60) accounts for when minutes reach 59   
        next_time = list(map(int,[minutes / 60 / 10, 
                                minutes / 60 % 10, 
                                minutes % 60 / 10,
                                minutes % 60 % 10]))
        
        isValid = True
        for d in next_time:
            if d not in digits_set:
                isValid = False
 
        if isValid:
            hh = str(int(minutes / 60))
            mm = str(int(minutes % 60))
            if len(hh) == 1:
                hh = "0" + hh
            if len(mm) == 1:
                mm = "0" + mm
            return hh + ":" + mm
    # Time: O(n * 4) = O(n) where n is up to 24 * 60; 4 comes from the loop through the 4 digits
    # Space: O(1) because at most we need to use set to store up to 4 digits


time = "19:34"
print(next_closest_time(time)) # expected output = "19:39"

time = "23:59"
print(next_closest_time(time)) # expected output = "22:22"


# Alternative approach from leetcode
class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = list(time.replace(":", ""))
        order = sorted(set(digits))
        
        #update last digit only
        pos = order.index(time[-1])
        if pos != len(order) - 1:
            return time[:-1] + order[pos + 1]
        
        #update last two digits
        pos = order.index(time[-2])
        if pos != len(order) - 1:
            next_digit = order[pos + 1]
            if int(next_digit) <= 5:
                return time[:-2] + next_digit + order[0]
        
        #update last three digits
        pos = order.index(time[1])
        if pos != len(order) - 1:
            next_digit = order[pos + 1]
            if (time[0] == "2" and int(next_digit) <= 3) or (time[0] != "2"):
                return time[0] + next_digit + ":" + order[0] * 2  
        
        #update all digits
        pos = order.index(time[0])
        if pos != len(order) - 1:
            next_digit = order[pos + 1]
            if int(next_digit) <= 2:
                return next_digit + order[0] + ":" + order[0]*2
        
        #change day
        return order[0]*2 + ":" + order[0]*2