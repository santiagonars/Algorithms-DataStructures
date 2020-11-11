# Given a binary tree, determine if it is a valid binary search tree (BST).

#Assume a BST is defined as follows:
#     -> The left subtree of a node contains only nodes with keys less than the node's key.
#     -> The right subtree of a node contains only nodes with keys greater than the node's key.
#     -> Both the left and right subtrees must also be binary search trees.

from BinarySearchTree import BinarySearchTree, Node

def main():
    tree = BinarySearchTree()
    arr = [2,1,3]
    for x in arr:
        tree.create(x)

    print("root node:", tree.root.info)
    print("left child node:", tree.root.left)
    print("right child node:", tree.root.right)

    print(isValidBST(tree.root))


def isValidBST(root):
    # input format must be tree node

    # return Bool
    pass

# NOTE: 
# One way to do that could be to write a function that returns a recursive function 
# that get's passed the root of the tree and checks that the if currentNode.left >= currentNode.right, then return false. 
# This function would return true only  if calling itselt on the currentNode.left and currentNode.right are both true.  
# At the beginning of that recursive function need too add a condition that checks if it's null, return true, 
#       meaning it searched every node passed the leaf and they all follow the conditions of a BST
# I think that would be O(N) time complexity since it's checking every value once

if __name__ == "__main__":
    main()