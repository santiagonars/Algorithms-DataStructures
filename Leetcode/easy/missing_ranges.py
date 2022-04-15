""" ------- Missing Ranges -------
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.
>>> A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. 
That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

        "a->b" if a != b
        "a" if a == b

Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74" 
[76,99] --> "76->99"

Example 2:
Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
 
Constraints:
    -109 <= lower <= upper <= 109
    0 <= nums.length <= 100
    lower <= nums[i] <= upper
    >>> All the values of nums are unique.
 """
def formatRange(lower_val, upper_val):
    if lower_val == upper_val:
        return str(lower_val)
    return str(lower_val) + "->" + str(upper_val)

def findMissingRanges(nums, lower, upper):
    missing_ranges = []
    prev = lower - 1
    for i in range(len(nums) + 1):
        curr = nums[i] if i < len(nums) else upper + 1
        if prev + 1 <= curr - 1:
            missing_ranges.append(formatRange(prev + 1, curr - 1))
        prev = curr
    return missing_ranges
    # Time: O(N) to traverse the nums array
    # Space: O(N) for list of missing ranges but not for any processing, so it could be O(1)

nums = [1,3,50,75]
lower, upper = 0, 99
print(findMissingRanges(nums, lower, upper)) # expected output = ["2","4->49","51->74","76->99"]

nums = [-1]
lower, upper = -1, -1
print(findMissingRanges(nums, lower, upper)) # expected output = []
