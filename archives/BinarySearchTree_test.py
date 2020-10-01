import unittest
from BinarySearchTree import BinarySearchTree, Node

class TestCases(unittest.TestCase):

    # test if values are equal
    def test1(self):
        tree = BinarySearchTree()
        tree.create(5)
        self.assertEqual(tree.root.info, 5, msg="Values not equal")

    def test2(self):
        tree = BinarySearchTree()
        tree.create(4)
        self.assertEqual(tree.root.info, 4, msg="Values not equal")

    # test below will fail
    def test3(self):
        tree = BinarySearchTree()
        tree.create(9)
        self.assertEqual(tree.root.info, 8, msg="Values not equal")


if __name__ == '__main__':
    unittest.main()