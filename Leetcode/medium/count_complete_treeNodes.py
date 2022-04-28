""" ------- Count Complete Tree Nodes -------
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, 
is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. 

*** It can have between 1 and 2h nodes inclusive at the last level h.

>>> Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1 

Constraints:
    The number of nodes in the tree is in the range [0, 5 * 104].
    0 <= Node.val <= 5 * 104
    The tree is guaranteed to be complete. """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" ----- SOLUTION: Linear time Recursion ----- """
def countNodes(root):
    return (1 + countNodes(root.left) + countNodes(root.right)) if root else 0
    # Time: O(N)
    # Space: O(logN) = O(d) for the recursion stack, where d is the tree depth


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(countNodes(root)) # expected output = 6

root = []
print(countNodes(root)) # expected output = 0

root = TreeNode(1)
print(countNodes(root)) # expected output = 1

print(10*"-")
""" ----- SOLUTION: Binary Search ----- 
>>> Tree is completely filled
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible.
"""

class Solution:
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists. 
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
        
    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0
        
        d = self.compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1
        
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2**d - 1) + left

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(s.countNodes(root)) # expected output = 6

root = []
print(s.countNodes(root)) # expected output = 0

root = TreeNode(1)
print(s.countNodes(root)) # expected output = 1



