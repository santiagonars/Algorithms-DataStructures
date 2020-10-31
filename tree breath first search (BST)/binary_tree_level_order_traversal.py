""" --------Binary Tree Level Order Traversal (easy)--------
Problem Statement #
>>> Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all 'nodes of each level from left to right' in separate sub-arrays.

Example 1:
input: binary tree: 1 -> 2 | 3 -> 4, 5 | 6, 7
output: [[1],[2,3],[4,5,6,7]]

Example 2:
input: binary tree: 12 -> 7 | 1 -> N, 9 | 10, 5
output: [[12],[7,1],[9,10,5]] """
# NOTE: Time complexity => O(N), where ‘N’ is the total number of nodes in the tree. 
#                       => This is due to the fact that we traverse each node once.
# NOTE: Space complexity => O(N) ,as we need to return a list containing the level order traversal.
#                        => will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes 
#                        => at any level  (this could happen only at the lowest level), 
#                        => therefore we will need O(N)O(N) space to store them in the queue.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverse(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue: # as long as queue is not empty
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            # if not children were added to queue the while loop will exit
        result.append(currentLevel)

    return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Level order traversal: " + str(traverse(root))) # expected output = [[1],[2,3],[4,5,6,7]]

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root))) # expected output = [[12],[7,1],[9,10,5]]


main()


# NOTE: Use Breadth First Search (BFS) technique
# - Need to traverse sall nodes of each level before moving onto the next level
""" >>> Use a Queue to efficiently traverse in BFS fashion """
#   1) Start by pushing the root node to the queue.
#   2) Keep iterating until the queue is empty.
#   3) In each iteration, first count the elements in the queue (let’s call it levelSize). 
#       We will have these many nodes in the current level.
#   4) Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
#   5) After removing each node from the queue, insert both of its children into the queue.
#   6) If the queue is not empty, repeat from step 3 for the next level.