""" --------Zigzag Traversal (medium)--------
Problem Statement #
>>> Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the same manner for the following levels. 

Example 1:
input: binary tree: 1 -> 2 | 3 -> 4, 5 | 6, 7
output: [[1],[3, 2],[4, 5, 6, 7]]  

Example 2:
input: binary tree: 12 -> 7 | 1 -> N, 9 | 10, 5 -> N, N | N, N | 20, 17 | N, N 
output: [[12],[1,7],[9,10,5],[17,20]] """
# NOTE: Time complexity => 0(N) ,for 'N' is the number of nodes in the tree
# NOTE: Space complexity => O(N) to return the results list and 0(N) for the queue.

from collections import deque # double linked list


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root): 
    result = []

    if root is None:
        return result
    
    # create a queue
    queue = deque()
    queue.append(root)
    level = 0
    """ leftToRight = True """ # NOTE: ALTERNATIVE
    # as long there are Nodes in the queue
    while queue:
        levelSize = len(queue)
        currentLevel = deque()
        level += 1
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # if 'currentNode' is even, append nodes in level from right to left 
            if level % 2 == 0:          
                currentLevel.appendleft(currentNode.val)           
            else: # if 'currentNode' is odd, append nodes in level from left to right (original order)
                currentLevel.append(currentNode.val)
            
            # NOTE: ALTERNATIVE
            """ # add the node to the current level based on the traverse direction
            if leftToRight:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val) """

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(list(currentLevel))
        """ leftToRight = not leftToRight """ # NOTE: ALTERNATIVE

    return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Zigzag traversal: " + str(traverse(root))) # expected output = [[1],[3, 2],[4, 5, 6, 7]] 

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root))) # expected output = [[12],[1,7],[9,10,5],[17,20]]


main()
