""" --------Binary Tree Inorder Traversal (medium)--------
Problem:
>>> Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2] 

Constraints:
>>> The number of nodes in the tree is in the range [0, 100].
>>> -100 <= Node.val <= 100
 

Follow up:
    Recursive solution is trivial, could you do it iteratively? """
# NOTE: Time complexity (Solution 1) => O(N)
# NOTE: Space complexity (Solution 1) => O(n) as the worst case. The average case is O(logN) where N is number of nodes.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []
        self.helper(root, result) 
        return result
     
    def helper(self, node, result):
        if node is not None:
                
            if node.left is not None:
                self.helper(node.left, result) 
                
            result.append(node.val) 
            
            if node.right is not None:
                self.helper(node.right, result)

from collections import deque
# iterative (using a stack)
class Solution2:
    def inorderTraversal(self, root: TreeNode):
        result = []
        if root is None:
            return result
        
        stack = deque()
        current = root
           
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            result.append(current.val)
            current = current.right
            
        return result


def main():
    # recursive
    sol = Solution()

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(sol.inorderTraversal(root))

    root = TreeNode(1)
    root.right = TreeNode(2)
    print(sol.inorderTraversal(root))

    # iterative (optimized)
    sol = Solution2()

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(sol.inorderTraversal(root))

    root = TreeNode(1)
    root.right = TreeNode(2)
    print(sol.inorderTraversal(root))


main()