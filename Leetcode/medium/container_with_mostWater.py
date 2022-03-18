""" ---------Container With Most Water---------
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
            In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1 """


# BRUTE FORCE SOLUTION:
def maxArea_2(height):
    max_area = 0
    for i in range(0, len(height)):
        for j in range(1, len(height)):
            currentArea = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, currentArea)
    return max_area
    # Time complexity: O(N^2)
    # Space complexity: O(1)


# OPTIMIZED SOLUTION: 
def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        currentArea = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, currentArea)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
    # Time: O(N)
    # Space: O(1)


height = [1,8,6,2,5,4,8,3,7] # expected output = 49
result = maxArea(height)
print(result)

height = [1,1] # expected output = 1
result = maxArea(height)
print(result)

height = [1,9,6,2,8,3] # expected output = 24
result = maxArea(height)
print(result)