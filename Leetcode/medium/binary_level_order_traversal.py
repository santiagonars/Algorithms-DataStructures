
""" -------  Binary Tree Level Order Traversal -------
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000 """

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" ----- SOLUTION: Recursion with BFS (Breath-First Search) ----- """
def levelOrder(root):
    levels = []
    if not root:
        return levels
    
    def helper(node, level):
        if len(levels) == level:
            levels.append([])
            
        levels[level].append(node.val)
        
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)
            
    helper(root, 0)
    return levels
    # TIME: O(N)
    # SPACE: O(N)

""" ----- SOLUTION: Iteration using a Queue ----- """
from collections import deque

def levelOrder(root):
    levels = []
    if not root:
        return levels

    level = 0
    queue = deque([root,])
    while queue:
        levels.append([])
        level_length = len(queue)

        for _ in range(level_length):
            node = queue.popleft()

            levels[level].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level += 1

    return levels
    # TIME: O(N) to traverse every node
    # SPACE: O(N) for the output
              
        
        

    

root = TreeNode(1)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left  = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root)) # expected output = [[3],[9,20],[15,7]]

root = TreeNode(1)
print(levelOrder(root)) # expected output = [[1]]

root = []
print(levelOrder(root)) # expected output = []
