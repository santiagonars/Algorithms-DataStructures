""" ----------Start of LinkedList Cycle (medium)----------
Problem Statement #
>>> Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle. """
# NOTE: Time complexity => O(N) 
# NOTE: Space complexity => O(1)
from __future__ import print_function


class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    cycle_length = 0
    # need to first find the linked list cycle
    slow, fast = head, head
    while fast is not None or fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast: # the cycle is found 
            cycle_length = calculate_cycle_length(slow)
            break
    return find_start(head, cycle_length)


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next 
        cycle_length += 1
        if current == slow: # move node until it has completed a full cycle
            break
    return cycle_length


def find_start(head, cycle_length):
    pointer1 = head
    pointer2 = head
    # move second pointer by length number of nodes in the cycle
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1
    # increment pointers 1 and 2 until they meet, which will be at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

main()