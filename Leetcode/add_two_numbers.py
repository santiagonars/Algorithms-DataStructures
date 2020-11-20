""" ----------Add Two Numbers----------
Problem:
>>> You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
>>> The number of nodes in each linked list is in the range [1, 100].
>>> 0 <= Node.val <= 9
>>> It is guaranteed that the list represents a number that does not have leading zeros. """
# Time complexity => O(max(M, N)) ,where 'M' and 'N' is the number of elements in the first and second list respectively.
#                 => recursion call is at most max(M, N) times.
# Space complexity => O(max(M, N)) ,for the new list it is at most max(M, N)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# recursive solution - !!!changes the original linked list by linking it to a bunch of zeros
def addTwoNumbers(l1, l2, c=0):

    sum_ = l1.val + l2.val + c
    c = sum_ // 10
    result_linkedList = ListNode(sum_ % 10)
    
    if (l1.next is not None or l2.next is not None or c != 0):
        if l1.next is None:
            l1.next = ListNode(0)
        if l2.next is None:
            l2.next = ListNode(0)
        result_linkedList.next = addTwoNumbers(l1.next, l2.next, c)
    
    return result_linkedList

# alternative mathematical solution
# BUG: 
def addTwoNumbers_2(l1, l2):
        digit_num1, digit_num2 = l1, l2
        result_before_head = ListNode()
        current = result_before_head
        c = 0 # carry

        while (digit_num1 is not None or digit_num2 is not None):

            if digit_num1 is not None:
                x = digit_num1.val
            else:
                x = 0
            if digit_num2 is not None:
                y = digit_num1.val
            else:
                y = 0

            sum_ = x + y + c
            c = sum_ // 10
            current.next = ListNode(sum_ % 10)
            current = current.next

            digit_num1 = digit_num1.next if digit_num1 else None
            digit_num2 = digit_num2.next if digit_num2 else None

        if c > 0:
            current.next = ListNode(c)

        return result_before_head.next


def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = addTwoNumbers(l1, l2)
    print("Two numbers added result is: ") # expected output = [7,0,8]
    while result != None:
        print(str(result.val) + " ", end='')
        result = result.next
    print()
    l3 = ListNode(9)
    l3.next = ListNode(9)
    l3.next.next = ListNode(9)
    l3.next.next.next = ListNode(9)
    l3.next.next.next.next = ListNode(9)
    l3.next.next.next.next.next = ListNode(9)
    l3.next.next.next.next.next.next = ListNode(9)
    
    l4 = ListNode(9)
    l4.next = ListNode(9)
    l4.next.next = ListNode(9)
    l4.next.next.next = ListNode(9)

    result = addTwoNumbers(l3, l4)
    print("Two numbers added result is: ") # expected output = [8,9,9,9,0,0,0,1]
    while result != None:
        print(str(result.val) + " ", end='')
        result = result.next


main()


