""" --------Binary Tree Path Sum (easy)--------
Problem Statement #
>>> Given a binary tree and a number ‘S’, 
find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’. 

Example 1:
Input: S = 10; binary tree: 1 -> 2 | 3 -> 4, 5 | 6, 7
Output: true
Explanation: The path with sum '10' is highlighted

Example 2-1:
Input: S = 23; binary tree: 12 -> 7 | 1 -> N, 9 | 10, 5
Output: true
Explanation: The path with sum '23' is highlighted

Example 2-2:
Input: S = 16; binary tree: 12 -> 7 | 1 -> N, 9 | 10, 5
Output: false
Explanation: There is no root-to-leaf path with sum '16'. """
# NOTE: Time complexity => O(N), where ‘N’ is the total number of nodes in the tree. 
#                       => This is due to the fact that we traverse each node once.
# NOTE: Space complexity => O(N) in the worst case to store the recursion stack.
#                       => Worst case will be when the given tree is a linked list where every node has only one child.

class TreeNode:
    def __init__ (self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if root is None:
        return False
    
    # if the current node is a leaf and its value is equal to the sum, we've found a path
    if root.val == sum and root.left is None and root.right is None:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive calls return true
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def main():
    # examples 2-1 and 2-2
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23))) # expected output = True
    print("Tree has path: " + str(has_path(root, 16))) # expected output = False


main()

# NOTE: To recursively traverse a binary tree in a DFS fashion, 
#        we can start from the root and at every step, 
#        make two recursive calls one for the left and one for the right child.

# -----Steps for our Binary Tree Path Sum problem:-----
#     1.) Start DFS with the root of the tree.
#     2.) If the current node is not a leaf node, do two things:
#          - Subtract the value of the current node from the given number to get a new sum => S = S - node.value
#          - Make two recursive calls for both the children of the current node
#             with the new number calculated in the previous step.
#     3.) At every step, see if the current node being visited is a leaf node 
#           and if its value is equal to the given number ‘S’. If both these conditions are true,
#           we have found the required root-to-leaf path, therefore return true.
#     4.) If the current node is a leaf but its value is not equal to the given number ‘S’, return false.

