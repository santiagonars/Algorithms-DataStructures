# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from BinarySearchTree import BinarySearchTree, Node

def main():
    tree = BinarySearchTree()
    tree.create(7)
    tree.create(3)
    tree.create(10)
    tree.create(2)
    tree.create(8)
    tree.create(9)
    tree.create(6)
    tree.create(5)
    print("root node:", tree.root.info)
    print("left child node:", tree.root.left)
    print("right child node:", tree.root.right)

    print(maxDepth(tree.root))


def maxDepth(root):
    if not root:
        return 0
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))


if __name__ == '__main__':  
    main()