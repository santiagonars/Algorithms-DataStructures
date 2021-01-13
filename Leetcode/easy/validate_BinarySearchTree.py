""" ----------Validate Binary Search Tree----------
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4. """
# Time complexity => O(N)
# Space complexity => O(N)
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Most efficient solution
def isValidBST(root):
    return checkBST(root)

def checkBST(node, lower=-math.inf, upper=math.inf):
    # if it's a NULL
    if node is None:
        return True
    # conditions that invalidate it to be a BST
    if node.val <= lower or node.val >= upper:
        return False
    if checkBST(node.left, lower, node.val) is False:
        return False
    if checkBST(node.right, node.val, upper) is False:
        return False
    return True


# ALTERNATIVE solution - works but not the best way
def isValidBST_2(root):

    if root is None or (root.left is None and root.right is None):
        return True
    # conditions that invalidate to be a BST
    if root.right is None and root.left.val > root.val:
        return False
    if root.left is None and root.right.val < root.val:
        return False
    if root.left.val > root.val:
        return False
    if root.right.val < root.val:
        return False
    if isValidBST_2(root.left) is False or isValidBST_2(root.right) is False:
        return False
    return True


if __name__ == "__main__":
    root = TreeNode(2) 
    root.left = TreeNode(1) 
    root.right = TreeNode(3) 
    print("Is a valid BST: ", isValidBST(root)) # expected = True

    root = TreeNode(5) 
    root.left = TreeNode(1) 
    root.right = TreeNode(4) 
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(6) 
    print("Is a valid BST: ", isValidBST(root)) # expected = False

    # root = TreeNode(2) 
    # root.left = TreeNode(1) 
    # root.right = TreeNode(3) 
    # print("Is a valid BST: ", isValidBST_2(root)) # expected = True

    # root = TreeNode(5) 
    # root.left = TreeNode(1) 
    # root.right = TreeNode(4) 
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(6) 
    # print("Is a valid BST: ", isValidBST_2(root)) # expected = False
