""" ------- Find Duplicate Subtrees -------
Given the root of a binary tree, return all duplicate subtrees.

>>> For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 
Constraints:
    The number of the nodes in the tree will be in the range [1, 10^4]
    -200 <= Node.val <= 200 """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" ----- SOLUTION: DFS (PREORDER) ----- """
from collections import defaultdict

def findDuplicateSubtrees(root):
    def dfs(node):
        if node is None:
            return "."

        subtree = str(node.val) + "-" + dfs(node.left) + "-" + dfs(node.right)

        if count[subtree] == 1:
            duplicates.append(node)
        count[subtree] += 1
        return subtree
    
    count, duplicates = defaultdict(int), []
    dfs(root)
    return duplicates
    # Time: O(N) for all the nodes
    # Space: O(M) to store all unique subtrees in `count` dict


def printTree(root):
    if root is None:
        return
    if root:
        print(root.val, end=" ")
        printTree(root.left)
        printTree(root.right)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left  = TreeNode(4)
# root.right.left  = TreeNode(2)
# root.right.right = TreeNode(4)
# root.right.left.left  = TreeNode(4)
# result = findDuplicateSubtrees(root) # expect: [[2,4],[4]] -> list of root of subtrees
# for subtree in result:    
#     printTree(subtree)
#     print()


# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(1)
# result = findDuplicateSubtrees(root) # expect: [[1]]
# for subtree in result:    
#     printTree(subtree)
#     print()

#  [2,2,2,3,null,3,null]
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left  = TreeNode(3)
root.right.left  = TreeNode(3)
result = findDuplicateSubtrees(root) # expect: [[2,3],[3]]
for subtree in result:    
    printTree(subtree)
    print()