""" --------Subsets (easy)--------
Problem Statement #
>>> Given a set with distinct elements, find all of its distinct subsets.

Example 1:
Input: [1, 3]
Output: [], [1], [3], [1,3]

Example 2:
Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3] """
# NOTE: Time complexity => O(N * 2^N) ,where ‘N’ is the total number of elements in the input set. 
#                       => Since in each step the number of subsets doubles as we add each element 
#                       => to all the existing subsets, therefore there are O(2^N) subsets.
#                       => A new subset is constructed from an existing set, resulting in O(N * 2^N).
# NOTE: Space complexity => O(N * 2^N) , for any additional space used by the algorithm is for the output list.
#                        => Since we will have a total of O(2^N) subsets, and each subset can take up to O(N) space.


def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])
    for currentNumber in nums:
        # take all existing subsets and insert the current number in them to create new subsets
        n = len(subsets)
        for  i in range(n):
            # create a new subset from the existing subset and insert the current element to it
            set = list(subsets[i])
            set.append(currentNumber)
            subsets.append(set)

    return subsets


def main():
    # expected output = [], [1], [3], [1,3]
    print("Here is the list of subsets: " + str(find_subsets([1, 3]))) 
    
    # expected output = [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3]))) 


main()

# NOTE: Use the Breadth First Search (BFS) approach.
# start with an empty set, iterate through all numbers one-by-one, and add them to existing sets to create new subsets.
