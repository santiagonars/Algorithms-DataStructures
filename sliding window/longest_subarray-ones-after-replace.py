""" ----------Problem Statement----------
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.

Example 1:
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9. """
# NOTE: Time complexity => 
# NOTE: Space complexity =>

def length_of_longest_subarray(arr, k):
    max_length = 0
    window_start = 0
    highest_ones_count = 0

    for window_end in range(len(arr)):
        # count any ones inside subarray window
        if arr[window_end] == 1:
            highest_ones_count += 1

        if (window_end - window_start + 1 - highest_ones_count) > k:
            if arr[window_start] == 1:
                # remove from count because it's not inside the subarray window anymore
                highest_ones_count -= 1
            window_start += 1
            
        max_length = max(max_length, window_end - window_start + 1)
    return max_length



if __name__ == "__main__":
    array_test1 = [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    k = 2
    print("Length of the longest subarray: ", length_of_longest_subarray(array_test1, k)) # expected output = 6
    array_test2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3
    print("Length of the longest subarray: ", length_of_longest_subarray(array_test2, k)) # expected output = 9