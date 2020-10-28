""" ----------Triplet Sum Close to Target (medium)----------
Problem Statement #
>>> Given an array of unsorted numbers and a target number, 
find a triplet in the array whose sum is as close to the target number as possible, 
return the sum of the triplet. 
If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target. """
# NOTE: Time complexity => O(N^2) => sorting is O(N*logN) + searching for triplet is O(N^2)
#                                 => O(N*logN + N^2) is asymptotically equivalent to O(N^2)
# NOTE: Space complexity => O(N) => space for sorted array

import math

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = math.inf # infinity
    for i in range(len(arr)):
        left, right = i + 1, len(arr) - 1
        while left < right:
            # get the difference by subtracting the target sum from the current 3 pointers in the array
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:
                return target_sum - target_diff # returns sum of all numbers
            # handle the smallest sum  
            if abs(target_diff) < abs(smallest_difference) or \
                    (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):

                smallest_difference = target_diff

            if target_diff > 0:
                left += 1 # increase sum of triplets
            else:
                right -= 1 #decrease sum of triplets

    return target_sum - smallest_difference

if __name__ == "__main__":
    array_test = [-2, 0, 1, 2]
    target = 2
    print(triplet_sum_close_to_target(array_test, target)) # expected output = 1
    array_test = [-3, -1, 1, 2]
    target = 1
    print(triplet_sum_close_to_target(array_test, target)) # expected output = 0
    array_test = [1, 0, 1, 1]
    target = 100
    print(triplet_sum_close_to_target(array_test, target)) # expected output = 3

# NOTE: Need 3 values from input array whose sum is closests to the target value
# Iterate thru array 
#   Use pointers from the left and right index of the array to compare values to the iterable variable
#   While loop as long as left is pointer is less than right pointer
#       Get the target difference by getting the target value minus the values of the array for the left, right, and iterable
#       -> if the target difference is equal to 0, this will be the smallest diffence possible, 
#              then return the difference of the target difference from the target sum, which is the same as the sum of the triplets
#       -> if absolute value (abs) of the target difference is less than the absolute value of smallest difference
#              OR the abs of each the target difference and smallest difference is equal to each other
#              AND target difference is greater than the smallest diffence (meaning sum of the numbers is smaller)
#              then make the smallest difference equal to the current target difference
#       -> if the target difference is greater than 0, the sum of the triplets is smaller than the target sum,
#              then increase the triplets' sum by incrementing the left pointer
#       -> else the target diffrence is less than 0, the sum for triplets is bigger than the target sum,
#              then decrease the triplet's sum by decrementing the right pointer