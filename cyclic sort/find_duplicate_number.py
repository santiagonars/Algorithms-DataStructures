""" ----------Find the Duplicate Number (easy)----------
Problem Statement #
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 
>>> Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:
Input: [1, 4, 4, 3, 2]
Output: 4

Example 2:
Input: [2, 1, 3, 3, 5, 4]
Output: 3

Example 3:
Input: [2, 4, 1, 4, 4]
Output: 4
# -------------------Similar Problems-------------------
Problem: 
>>> Can we solve the above problem in O(1) space and without modifying the input array?

Solution: While doing the cyclic sort, we realized that the array will have a cycle due to the duplicate number 
and that the start of the cycle will always point to the duplicate number. 
This means that we can use the fast & the slow pointer method to find the duplicate number 
or the start of the cycle similar to Start of LinkedList Cycle. """
# NOTE: Time complexity => O(N)
# NOTE: Space complexity => O(1) but modifies input array


def find_duplicate(nums):
    i = 0
    while i < len(nums):
        # first check if number is in the correct location
        if nums[i] != i + 1: # add 1 because range starts at 1
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i] # there is only one duplicate
        else:
            i += 1
    return -1

# Solution in O(1) space without needing to modify the input array; the start of the cycle will always point to the duplicate number
def find_duplicate_without_modifying(arr):
    slow, fast = arr[0], arr[arr[0]]
    while slow != fast: # they meet bc there's a cycle due to the duplicate
        slow = arr[slow]
        fast = arr[arr[fast]]

    # find cycle length
    current = arr[arr[slow]]
    cycleLength = 1
    while current != arr[slow]:
        current = arr[current]
        cycleLength += 1

    return find_start(arr, cycleLength)

def find_start(arr, cycleLength):
    pointer1, pointer2 = arr[0], arr[0]
    # move pointer2 ahead 'cycleLength' steps
    while cycleLength > 0:
        pointer2 = arr[pointer2]
        cycleLength -= 1

    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = arr[pointer1]
        pointer2 = arr[pointer2]

    return pointer1


def main():
    print(find_duplicate([1, 4, 4, 3, 2])) # expected output = 4
    print(find_duplicate([2, 1, 3, 3, 5, 4])) # expected output = 3
    print(find_duplicate([2, 4, 1, 4, 4])) # expected output = 4
    print("----")
    print(find_duplicate_without_modifying([1, 4, 4, 3, 2])) # expected output = 4
    print(find_duplicate_without_modifying([2, 1, 3, 3, 5, 4])) # expected output = 3
    print(find_duplicate_without_modifying([2, 4, 1, 4, 4])) # expected output = 4


main()

# NOTE: The is only ONE DUPLICATE! 
# - if while swapping the number with its index both the numbers being swapped are same, we have found the duplicate!

