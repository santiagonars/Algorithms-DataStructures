""" --------Sum of Path Numbers (medium)--------
Problem Statement #
>>> Given a binary tree where each node can only have a digit (0-9) value, 
each root-to-leaf path will represent a number. 
***Find the total sum of all the numbers represented by all paths. 

Example 1:
Input: binary tree: 1 -> 7 | 9 -> N, N | 2, 9
Output: 408 
Explanation: The sum of all path numbers => 17 + 192 + 199

Example 2:
Input: binary tree: 1 -> 0 | 1 -> 1, N | 6, 5
Output: 332 
Explanation: The sume of all path numbers => 101 + 116 + 115 """
# NOTE: Time complexity => O(N) ,where 'N' is the number of nodes
#                       => 
# NOTE: Space complexity => O(N) in the worst case; used to store the recursion stack.
#                        => worst case is when the input tree is a linked list (ex. every node has only one child).


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_digits(root):
    return find_root_to_leaf_path_numbers(root, 0)


def find_root_to_leaf_path_numbers(currentNode, pathSum):
    if currentNode is None:
        return 0

    # calculate the path number of the current node
    pathSum = 10 * pathSum + currentNode.val

    # if the current node is a leaf, return the current path sum
    if currentNode.left is None and currentNode.right is None:
        return pathSum

    # traverse the left and the right sub-tree
    return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + find_root_to_leaf_path_numbers(currentNode.right, pathSum) 
    

# ALTERNATION SOLUTION:
def find_sum_of_path_digits_2(root):
    sum = 0
    sum = find_path_sum_recursive(root, "", sum)
    return sum


def find_path_sum_recursive(currentNode, currentPath_digit, sum):
    if currentNode is None:
        return 0

    #concatenate digit value of node for the current path
    currentPath_digit += str(currentNode.val)

    if currentNode.left is None and currentNode.right is None:
        sum += int(currentPath_digit)
    else:
        sum1 = 0
        sum2 = 0
        # traverse left sub-tree
        sum1 = find_path_sum_recursive(currentNode.left, currentPath_digit, sum)
        # traverse right sub-tree
        sum2 = find_path_sum_recursive(currentNode.right, currentPath_digit, sum)
        sum += sum1 + sum2

    return sum


def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_digits(root))) # expected output = 408
    print("Total Sum of Path Numbers (ALT): " + str(find_sum_of_path_digits_2(root))) # expected output = 408

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_digits(root))) # expected output = 332
    print("Total Sum of Path Numbers (ALT): " + str(find_sum_of_path_digits_2(root))) # expected output = 332


main()

# NOTE:Find every every path and add up the digits values in every node in the path to represent a number; then add them.