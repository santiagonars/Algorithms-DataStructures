""" ----------Middle of the LinkedList (easy)----------
Problem Statement #
>>> Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
*** If the total number of nodes in the LinkedList is even, return the second middle node.

Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Example 2:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4

Example 3:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4 """
# NOTE: Time complexity => O(N)
# NOTE: Space complexity => O(1), it is costant space

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list2(head):
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow

# alternative approach using more space for returning the value
def find_middle_of_linked_list(head):
    slow, fast = head, head
    middle_node = head
    
    while fast is not None or fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast is None: # last number is even: fast will be null an slow will be middle (it is the second middle)
            middle_node = slow
            break
        if fast.next is None: # last number is odd: fast.next will be null and slow will be the middle
            middle_node = slow
            break
    return middle_node


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Middle Node: " + str(find_middle_of_linked_list(head).value)) # expected output = 3

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value)) # expected output = 4

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value)) # expected output = 4


main()