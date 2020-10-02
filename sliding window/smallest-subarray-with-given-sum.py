""" Problem Statement #
Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0, if no such subarray exists.

Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6]. """
# NOTE: Time complexity => O(N) => it is actually O(N+N) which is asymptotically equivalent to O(N)
#                          The outer for loop runs for all elements and the inner while loop processes each element only once.
# NOTE: Space complexity => O(1)

import math

def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_length = math.inf
    window_start_index = 0

    for window_end_index in range(len(arr)):
        window_sum += arr[window_end_index] # add the next element
        # make window smaller until 'window_sum' is smaller than s
        while window_sum >= s:
            min_length = min(min_length, window_end_index - window_start_index + 1) # needed to add 1 because index started at 0
            window_sum -= arr[window_start_index]
            window_start_index += 1
    if min_length == math.inf:
        return 0
    return min_length

if __name__ == '__main__':
    arraytest1 = [2, 1, 5, 2, 3, 2]
    s = 7
    print(smallest_subarray_with_given_sum(s, arraytest1)) # expected output = 2
    arraytest2 = [2, 1, 5, 2, 8]
    s = 7
    print(smallest_subarray_with_given_sum(s, arraytest2)) # expected output = 1
    arraytest3 = [3, 4, 1, 1, 6]
    s = 8
    print(smallest_subarray_with_given_sum(s, arraytest3)) # expected output = 3