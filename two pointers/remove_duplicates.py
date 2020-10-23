""" ----------Remove Duplicates (easy)----------
>>> Problem Statement:
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; 
after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11]. """
# NOTE: Time complexity => O(N) => to loop through the all the numbers in the array
# NOTE: Space complexity => O(1) => cosntant because we only track the index value in the array of next_non_duplicate

# point top 
def remove_duplicates(arr):
    next_non_duplicate = 1

    i = 1
    while (i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    print(arr[:next_non_duplicate])
    return next_non_duplicate


if __name__ == "__main__":
    array_test = [2, 3, 3, 3, 6, 9, 9] # REMEMBER it's sorted!
    print(remove_duplicates(array_test)) # expected output = 4
    array_test = [2, 2, 2, 11]
    print(remove_duplicates(array_test)) # expected output = 2