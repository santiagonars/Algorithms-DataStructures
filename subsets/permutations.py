""" --------Permutations (medium)--------
Problem Statement #
>>> Given a set of distinct numbers, find all of its permutations.

* Permutation is defined as the re-arranging of the elements of the set. 

For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}

>>> *** If a set has ‘n’ distinct elements it will have n! permutations.

Example 1:
Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1] """
# NOTE: Time complexity => O(N * N!) .There are N! permutations and we are using 2 for loops to iterate through all permutations. 
#                       => To insert a number in each permutation is size N will take O(N).
# NOTE: Space complexity => O(N * N!) ,for the result list and the queue to store the intermediate permutations.
#                        => The overall space to store N! permutations each containing N elements will be O(N*N!)


from collections import deque


def find_permutations(nums):
    numsLength = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for currentNumber in nums:
        # take all existing permutations and add the current number to create new permutations
        n = len(permutations)
        for _ in range(n):
            oldPermutation = permutations.popleft()
            # create a new permutation by adding the current number at every position
            for j in range(len(oldPermutation)+1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, currentNumber)
                if len(newPermutation) == numsLength:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)

    return result


# ALTERNATIVE: Recursive solution---------------------------------
def generate_permutations(nums):
    result = []
    generate_permutations_recursive(nums, 0, [], result)
    return result


def generate_permutations_recursive(nums, index, currentPermutation, result):
    if index == len(nums):
        result.append(currentPermutation)
    else:
        # create a new permutation by adding the current number at every position
        for i in range(len(currentPermutation)+1):
            newPermutation = list(currentPermutation)
            newPermutation.insert(i, nums[index])
            generate_permutations_recursive(nums, index + 1, newPermutation, result) # recursive function 
# --------------------------------------------------------------

def main():
    # expected output = [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
    # expected output = [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
    print("Here are all the permutations: " + str(generate_permutations([1, 3, 5])))


main()


