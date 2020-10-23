""" ----------Cyclic Sort (easy)----------
Problem Statement #
We are given an array containing ‘n’ objects. 
Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. 
This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

>>> Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space.

***For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, 
though each number is actually an object.

Example 1:
Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]

Example 2:
Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]

Example 3:
Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6] """
# NOTE: Time complexity => O(N), Eventhough we are not incrementing i when swapping the numbers, which results more than 'N' iterations
#                       => but in worse case scenario, the while loop will swap a total of ‘n-1’ numbers 
#                       => and once a number is at its correct index, we will move on to the next number by incrementing i
#                       => Hence it will take O(N) + O(N + 1) which is asymptotically equivalent to O(N)
# NOTE: Space complexity => O(1)


def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1 # number should be (index + 1) because we array starts at 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i] # swap numbers
        else:
            i += 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2])) # expected output = [1, 2, 3, 4, 5]
    print(cyclic_sort([2, 6, 4, 3, 1, 5])) # expected output = [1, 2, 3, 4, 5, 6]
    print(cyclic_sort([1, 5, 6, 4, 3, 2])) # expected output = [1, 2, 3, 4, 5, 6]


main()

# NOTE: The input array contains numbers in the range of 1 to ‘n’, IT CAN BE SORTED EFFICIENTLY!
# - all numbers are unique, so try placing each number at its correct place.
# - loop thru array one number (object) at a time
#   => As long as number is not in correct index, sway it with the number that is it's correct index
#         This will go through all numbers and place them in their correct indices, hence, sorting the whole array.
