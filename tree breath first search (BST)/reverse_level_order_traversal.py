""" --------Reverse Level Order Traversal (easy)--------
Problem Statement #
>>> Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
 i.e., the lowest level comes first. 
You should populate the values of all nodes in each level from left to right in separate sub-arrays. 
Example 1:
input: binary tree: 1 -> 2 | 3 -> 4, 5 | 6, 7
output: [[4,5,6,7], [2,3], [1]]

Example 2:
input: binary tree: 12 -> 7 | 1 -> 9 | 10, 5
output: [[9,10,5], [7,1], [12]] """
# NOTE: Time complexity => O(N) ,where 'N' is the number of nodes in the binary tree
# NOTE: Space complexity => O(N) ,to return the list of nodes of in reverse level-by-level traversal order.
#                        => Will also need O(N) space for the queue, where each level will need a max of O(N/2) space.
from collections import deque

class TreeNode:
    def __init__ (self, val):
        self.val = val
        self.left, self.right = None, None


def reverse_traverse(root):
    result = deque()
    
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add node to the current level list
            currentLevel.append(currentNode.val)
            # insert node children in queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.appendleft(currentLevel)

    return list(result)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(reverse_traverse(root))) # expected output = [[9,10,5], [7,1], [12]]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Level order traversal: " + str(reverse_traverse(root))) # expected output = [[4,5,6,7], [2,3], [1]]


main()