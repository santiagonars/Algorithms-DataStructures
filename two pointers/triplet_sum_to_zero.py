""" ----------Triplet Sum to Zero (medium)----------
Problem Statement:
>>> Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero. """
# NOTE: Time complexity => O(N^2) => sorting is O(N*logN). searchPair() is O(N).
#                                 => searchPair() is called for every number in searchTriplets() which is O(N^2)
#                                 => sorting + searchTriplets() = O(N*logN + N^2) which is considered O(N^2)
# NOTE: Space complexity => O(N) => spaced required for sorting. 


def search_triplets(arr):
    arr.sort() # need to sort the array to skip duplicates
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue # skip duplicate for the'target_sum' value
        search_pair(arr, -arr[i], i + 1, triplets)

    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            # slide each left and right pointer to check if the next one is a duplicate
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1 # avoid duplicates by skipping element
            while left < right and arr[right] == arr[right + 1]:
                right -= 1 # avoid duplicates by skipping element
        elif target_sum > current_sum:
            left += 1
        else:
            right -= 1


if __name__ == "__main__":
    array_test = [-3, -3, 0, 1, 2, -1, 1, -2]
    print(search_triplets(array_test)) # expected output = [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
    array_test = [-5, 2, -1, -2, 3]
    print(search_triplets(array_test)) # expected output = [[-5, 2, 3], [-2, -1, 3]]


# NOTE: If X + Y + Z == 0, then X + Z == -Y. Knowing this, we can find a a pair for X and Y that equal negative Z, a target sum.
#       -> We need to compare the sum of all pairs that equal the target sum  by pointing to each end of the array
#       -> If the target sum is greater, then increase the index value of the left end of the array
#       -> If the target sum is lower, then decrease the index value of the right end of the array 
#       -> If target sum is equal, then we have a match for 3 value that equal 0 [target_sum, left_pointer_arr, right_pointer_arr]
#           -> Also as long as each left & right pointer is the same value that the it's respective previous one in the array, 
#               sliding the pointers by either incrementing the left or decrementing right pointers (hence do for each one)
# REMEMBER: Duplicates matter because triplets have to be unique!