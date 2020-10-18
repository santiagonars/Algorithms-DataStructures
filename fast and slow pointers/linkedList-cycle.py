""" ----------LinkedList Cycle (easy)----------
Problem #1 (boolean problem)
>>> Given the head of a Singly LinkedList, 
write a function to determine if the LinkedList has a cycle in it or not. 
#-----------------------------------------------------------------------------
Problem #2 (Find length problem) 
>>> Given the head of a LinkedList with a cycle, find the length of the cycle.

Solution: 
We can use the solution for problem #1 to find the cycle in the LinkedList. Once the fast and slow pointers meet, 
we can save the slow pointer and iterate the whole cycle with another pointer 
until we see the slow pointer again to find the length of the cycle. """

# NOTE: Time complexity => O(N) => N is the number of nodes in linked list (for both ploblems #1 and #2)
# NOTE: Space complexity => O(1) => (for both ploblems #1 and #2)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True # the cycle is found because the 2 pointers met
    return False


def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None or fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return calculate_cycle_length(slow)
    return 0


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList cycle length: " + str(find_cycle_length(head)))
    

main()