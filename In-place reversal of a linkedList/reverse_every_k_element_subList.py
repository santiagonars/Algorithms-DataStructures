""" ----------Reverse every K-element Sub-list (medium)----------
Problem Statement #
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too. """
# NOTE: Time complexity => O(N) ,where ‘N’ is the total number of nodes in the LinkedList
# NOTE: Space complexity => O(1) ,since we only used constant space 
from __future__ import print_function

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_every_k_elements2(head, k):
    if k <= 1 or head is None:
        return head

    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        # after reversing, 'current' which is now the first element in the sub-list will become the last node of the sub-list 
        last_node_of_sub_list = current
        next = None # will be used to temporarily store the next node
        i = 0
        while current is not None and i < k: # reverse 'k' nodes
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # connect with previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous # points to the new previous which is now the first node in the sub-list
        else:
            head = previous

        # connect with the next part
        last_node_of_sub_list.next = current # points to the new current which is is now after and outside of 'k'

        if current is None:
            break
        previous = last_node_of_sub_list # position previous to the node before 'current'
    return head

def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        # after reversing the LinkedList 'current' will become the last node of the sub-list
        last_node_of_sub_list = current
        next = None  # will be used to temporarily store the next node
        i = 0
        while current is not None and i < k:  # reverse 'k' nodes
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # connect with the previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        # connect with the next part
        last_node_of_sub_list.next = current

        if current is None:
            break
        previous = last_node_of_sub_list
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()

# NOTE: K is the size of sublist to be reversed
# The problem follows the In-place Reversal of a LinkedList pattern and is quite similar to Reverse a Sub-list. 
# The only difference is that we have to reverse all the sub-lists. 
# We can use the same approach, starting with the first sub-list (i.e. p=1, q=k) 
# and keep reversing all the sublists of size ‘k’.