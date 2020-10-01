""" # ---Problem Statement---
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4]. """
# NOTE: Time complexity => O(N)
# NOTE: Space complexity => O(1)

def max_sub_array_of_size_k(k, arr):
    #Find the maximum sum of any continious subarray
    #define the number that will become the maximum value
    maxValue = 0
    totalSum = 0
    startofWindow = 0
    for endOfWindow in range(len(arr)):
        totalSum += arr[endOfWindow] # add the next element
        # slide window until the size of 'k' (start from 0)
        if endOfWindow >= k - 1: 
            # change the max value if is less than the total sum
            if maxValue < totalSum: 
                maxValue = totalSum
            
            totalSum -= arr[startofWindow] # subtract the first element
            startofWindow += 1
    return maxValue


if __name__ =='__main__':
    arraytest1 = [2, 1, 5, 1, 3, 2] 
    k=3 
    print(max_sub_array_of_size_k(k,arraytest1)) # expected output = 9

    arraytest2 = [2, 3, 4, 1, 5]
    k=2 
    print(max_sub_array_of_size_k(k,arraytest2)) # expected output = 7