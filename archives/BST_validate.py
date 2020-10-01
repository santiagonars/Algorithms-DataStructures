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


if __name__ == "__main__":
    main()