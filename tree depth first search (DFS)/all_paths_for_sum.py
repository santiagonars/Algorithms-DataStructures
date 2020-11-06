""" --------All Paths for a Sum (medium)--------
Problem Statement #
>>> Given a binary tree and a number ‘S’, 
find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

Example 1:
Input: S = 12; 
Output: [[1, 7, 4], [1, 9, 2]]
Explanation: There are the two paths with sum '12' =>  1 -> 7 -> 4 and 1 -> 9 -> 2

Example 2:
Input: S = 23; binary tree: 12 -> 7 | 1 -> N, 9 | 10, 5
Output: [[12, 7, 4], [12, 1, 10]]
Explanation: There are the two paths with sum '23' =>  12 -> 7 -> 4 and 12 -> 1 -> 10 
--------------------------------------------------------------------------------------------------
Similar Problems #
Problem 1: Given a binary tree, return all root-to-leaf paths.
Solution: We can follow a similar approach. We just need to remove the “check for the path sum”.

TODO: Problem 2: Given a binary tree, find the root-to-leaf path with the maximum sum.
Solution: We need to find the path with the maximum sum. 
As we traverse all paths, we can keep track of the path with the maximum sum."""
# NOTE: Time complexity => O(N^2) ,where ‘N’ is the total number of nodes in the tree.
#                       => This because we traverse each node once (which will take O(N)), 
#                       => and for every leaf node we might have to store its path which will take O(N) -> appending a list to a list
#                       => ^ this is the case where the depth (height of the tree) is equivalent to 'N'
#                       =>  We can have O(NlogN) time complexity in a balanced tree.
# NOTE: Space complexity => O(N) if we ignore the space required for 'allPaths', in the worst case.
#                        => O(N*logN) , for the overall space complexity of the algorithm.
#                        => Since the depth (or height) of a balanced binary tree is O(logN)
#                        => we can say that at the most, each path can have logN nodes in it.
#                        => This means that the total size of the allPaths list will be O(N*logN)O(N∗logN).
#                        => If the tree is not balanced, we will still have the same worst-case space complexity.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, required_sum):
    allPaths = []
    find_paths_recursive(root, required_sum, [], allPaths)
    return allPaths


def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
    if currentNode is None:
        return

    # add the current node to the path
    currentPath.append(currentNode.val)

    # if the current node is a leaf and its value is equal to required_sum, save the current path
    if currentNode.val == required_sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        # traverse the left sub-tree
        find_paths_recursive(currentNode.left, required_sum - currentNode.val, currentPath, allPaths)
        # traverse the right sub-tree
        find_paths_recursive(currentNode.right, required_sum - currentNode.val, currentPath, allPaths)

    del currentPath[-1] # removes last value (from the right) from the list; same as using .pop()


def main():
    # example 2
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))
    # expected output = [[12, 7, 4], [12, 1, 10]]

main()


# NOTE: follow a DFS approach similar ro the problem Binary Tree Path Sum, except:
#  - Every time we find a root-to-leaf path, we will store it in a list.
#  - We will traverse all paths and will not stop processing after finding the first path.