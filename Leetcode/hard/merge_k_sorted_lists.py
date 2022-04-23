""" ------- Valid Parenthesis -------
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
>>> Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:
    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104. """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

""" ---------- SOLUTION: Optomizes using a Priority Queue using heapq ---------- """
import heapq

class SolutionHeapq:
    def mergedKLists(self, lists):
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h) # turn h into a min heap
        head = cur = ListNode(None)

        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next 
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next
        # Time: O(k*LogN) where N is the number of nodes and k is the number of linked lists
        # Space: O(N) cost to create create a new linked list
        #        O(k) for the heapq


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)
lists = [l1, l2, l3]
s = SolutionHeapq()
result = s.mergedKLists(lists) 
ans = []
while result:
    ans.append(result.val)
    result = result.next
print(ans) # expected output = [1,1,2,3,4,4,5,6]

# lists = [[]]
# print(mergedLists(lists)) # expected output = []


""" ---------- SOLUTION: Brute force ---------- """
class SolutionBruteForce:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0) # set a dummy value
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
        # Time: O(N*LogN) to sort the the values
        # Space: O(N) - sorting costs O(N); ccreating a new linked lists costs O(N)

""" 
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)
lists = [l1, l2, l3]
s = SolutionBruteForce()
result = s.mergeKLists(lists) 
ans = []
while result:
    ans.append(result.val)
    result = result.next
print(ans) # expected output = [1,1,2,3,4,4,5,6] """