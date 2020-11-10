""" --------Subsets With Duplicates (easy)--------
Problem Statement #
>>> Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:
Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

Example 2:
Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] """
# NOTE: Time complexity => O(N * 2^N) ,where ‘N’ is the total number of elements in the input set. 
#                       => Since in each step the number of subsets doubles (if not duplicate) as we add each element 
#                       => to all the existing subsets, therefore there are O(2^N) subsets.
#                       => A new subset is constructed from an existing set, resulting in O(N * 2^N).
# NOTE: Space complexity => O(N * 2^N) , for any additional space used by the algorithm is for the output list.
#                        => Since we will have a total of O(2^N) subsets, and each subset can take up to O(N) space.


def find_subsets(nums):
    # sort numbers to handle the duplicates
    list.sort(nums)
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0 # represent which subsets to copy from 'subsets' to create new subsets from to add a current number to
    for i in range(len(nums)):
        startIndex = 0
        # if current and previous elements are the same, create new subsets from only the susbets added in the previous step
        if i > 0 or nums[i] == nums[i - 1]:
            startIndex = endIndex + 1 # for duplicate it will start where the previous step index ended
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex + 1):
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)

    return subsets


def main():
    # expected output = [], [1], [3], [1,3], [3,3], [1,3,3]
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    # expected output = [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

# NOTE: Similar to solution in 'subsets.py' problem except:
#   1.) Sort all numbers of the given set. This will ensure that all duplicate numbers are next to each other.
#   2.) Follow the same BFS approach but whenever we are about to process a duplicate 
#       (i.e., when the current and the previous numbers are same), 
#       instead of adding the current number (which is a duplicate) to all the existing subsets, 
#       only add it to the subsets which were created in the previous step.