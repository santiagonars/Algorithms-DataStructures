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


""" ----- SOLUTION: ALTERNATIVE solution - works but not the best way ----- """
# def isValidBST(root):

#     if root is None or (root.left is None and root.right is None):
#         return True
#     # conditions that invalidate to be a BST
#     if root.right is None and root.left.val > root.val:
#         return False
#     if root.left is None and root.right.val < root.val:
#         return False
#     if root.left.val > root.val:
#         return False
#     if root.right.val < root.val:
#         return False
#     if isValidBST(root.left) is False or isValidBST(root.right) is False:
#         return False
#     return True


""" ----- SOLUTION: Simple solution (Not very efficient)----- """
# def isValidBST(root):
#     return checkBST(root)

# def checkBST(node, lower=-math.inf, upper=math.inf):
#     # if it's a NULL
#     if node is None:
#         return True
#     # conditions that invalidate it to be a BST
#     if node.val <= lower or node.val >= upper:
#         return False
#     if not checkBST(node.left, lower, node.val):
#         return False
#     if not checkBST(node.right, node.val, upper):
#         return False
#     return True


""" ----- SOLUTION: Recursive Traversal with Valid Range ----- """
def isValidBST(root):
    def validate(node, lower=-math.inf, upper=math.inf):
        if node is None:
            return True
        
        if node.val <= lower or node.val >= upper:
            return False
        return (validate(node.left, lower, node.val)) and (validate(node.right, node.val, upper))

    return validate(root)
    # O(N) time for recursive call for every node
    # O(N) space to store the calls the calls of the entire tree


""" ----- SOLUTION: Iterative Traversal with Valid Range -----
Uses a stack (for BFS) instead of recursition
For this problem, recursion works better """
def isValidBST(root):
    if not root:
        return True
    
    stack = [(root, -math.inf, math.inf)]
    while stack:
        root, lower, upper = stack.pop()
        if not root:
            continue
        val = root.val
        if val <= lower or val >= upper:
            return False
        stack.append((root.left, lower, val))
        stack.append((root.right, val, upper))
    return True
    # Time: O(N) to go through every node
    # Space: O(N) append the tree to stack





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

