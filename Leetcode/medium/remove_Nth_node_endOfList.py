""" ------- Remove Nth Node From End of List -------
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

>>> Follow up: Could you do this in one pass? """

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

""" ----- SOLUTION 1:  ----- """

def removeNthFromEnd(head, n):
    len = 0
    dummy = ListNode(0)
    dummy.next = head
    pointer = head

    while pointer:
        len += 1
        pointer = pointer.next

    pointer = dummy
    len -= n
    while len > 0:
        len -= 1
        pointer = pointer.next
    
    pointer.next = pointer.next.next
    return dummy.next
    # O(N) where L = N, & first traverses O(L) to count length and then O(L - n) to arrive at the node before
    # O(1)

""" ----- SOLUTION 2: FASTER ----- """
def removeNthFromEnd(head, n):
    len = 0
    currentNode = head

    while currentNode:
        len += 1
        currentNode = currentNode.next
    # account for edges cases where there is only 1 node or need to remove the first node
    if len == n:
        return head.next

    currentNode = head
    nodeBeforeRemovedIndex = len - n - 1
    for _ in range(nodeBeforeRemovedIndex):
        currentNode = currentNode.next
    
    currentNode.next = currentNode.next.next
    return head
    # O(N)
    # O(1)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2
result = removeNthFromEnd(head, n)
print("Result is: ") # expected output = [1,2,3,5]
while result:
    print(str(result.val) + " ", end='')
    result = result.next
print()
# ---------------------------------------------------------------
head = ListNode(1)
n = 1
result = removeNthFromEnd(head, n)
print("Result is: ") # expected output = []
while result:
    print(str(result.val) + " ", end='')
    result = result.next
print()
# # ---------------------------------------------------------------
head = ListNode(1)
head.next = ListNode(2)
n = 1
result = removeNthFromEnd(head, n)
print("Result is: ") # expected output = [1]
while result:
    print(str(result.val) + " ", end='')
    result = result.next
