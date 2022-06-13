""" ------- Binary Tree Zigzag Level Order Traversal -------
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 
Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100 """

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" ----- SOLUTION: Stacks ----- """
def zigzagLevelOrder(root):
    if not root:
        return
    
    # 2 stacks
    current_level = []
    next_level = []
    
    fromLeft = True # push nodes from left of tree if true, from right of tree if false
    
    result = []
    current_traversal = []
    current_level.append(root)

    while len(current_level) > 0:
        
        node = current_level.pop()
        # print(node.val)
        current_traversal.append(node.val)

        if fromLeft:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        else:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)

        if len(current_level) == 0:
            fromLeft = not fromLeft
            current_level, next_level = next_level, current_level
            result.append(current_traversal)
            current_traversal = []

    return result
    # Time: O(N)
    # Space: O(N)

""" ----- SOLUTION: Queue ----- """
from collections import deque
def zigzagLevelOrder2(root):
    levels = []

    if not root:
        return levels

    queue = deque([root])

    while queue:
        next_level = deque()
        level_length = len(queue)

        for _ in range(level_length):
            node = queue.popleft()
            if len(levels) % 2:
                next_level.appendleft(node.val)
            else:
                next_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        levels.append(list(next_level))
    return levels
    # Time: O(N)
    # Space: O(N)

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(zigzagLevelOrder(tree))
print(zigzagLevelOrder2(tree))