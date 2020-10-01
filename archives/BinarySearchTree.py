# Node class
class Node:
    def __init__(self, info): 
        self.info = info
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# test that first value is equal to second value
def testcase(first, second):
    if first == second:
        print(True)
    else:
        print(False)

def main():
    tree = BinarySearchTree()
    tree.create(5)
    tree.create(3)
    tree.create(8)

    testcase(tree.root.info, 5)
    print("left child node:", tree.root.left)
    print("right child node:", tree.root.right)

if __name__ == '__main__':  
    main()
