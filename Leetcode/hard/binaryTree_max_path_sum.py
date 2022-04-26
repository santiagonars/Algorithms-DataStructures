""" ------- Binary Tree Maximum Path Sum -------
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
in the sequence has an edge connecting them. A node can only appear in the sequence at most once. 
NOTE: Note that the path does not need to pass through the root.

*** The path sum of a path is the sum of the node's values in the path.

>>> Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 
Constraints:
    The number of nodes in the tree is in the range [1, 3 * 104].
    -1000 <= Node.val <= 1000
 """

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" ----- SOLUTION: Recursion ----- """
def maxPathSum(root):
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
                    
        max_gain_newpath = node.val + left_gain + right_gain
                    
        max_sum = max(max_sum, max_gain_newpath)
        
        return node.val + max(left_gain, right_gain)
        
    max_sum = float('-inf')
    max_gain(root)
    return max_sum

    # Time:  O(N) where N is the number of nodes
    # Space: O(H) where H is the height of the tree for the number of recursive calls
    #        O(logN) for a balanced tree H = logN
    #        O(N) for worse case H = N


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(maxPathSum(root)) # expected output = 6

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxPathSum(root)) # expected output = 42 

