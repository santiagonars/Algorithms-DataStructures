""" ----------Merge K Sorted Lists (medium)----------
Problem Statement #
>>> Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:
Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9] """
# Time complexity => O(N*logK) . To go through all the elements in the arrays + remove/add one elemtn to the heap for each
#                 => where ‘N’ is the total number of elements in all the ‘K’ input arrays.
# Space complexity => O(K) becasue the min-heap will store one number from all the 'K' input arrays
from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # used for the min-heap (for linked lists)
    def __lt__(self, other):
        return self.value < other.value 


def merge_lists(lists):
    minHeap = []
    # put the root of each list in the min-heap
    for root in lists:
        if root is not None:
            heappush(minHeap, root)
  
    # take the smallest(top) element from the min-heap and add it to the result (NOTE: Creating a result linked-list)
    # if the top element has a next element add it to the heap 
    resultHead, resultTail= None, None 
    while minHeap: 
        node = heappop(minHeap)
        if resultHead is None:
            resultHead  = resultTail = node
        else:
            resultTail.next = node
            resultTail = resultTail.next

        if node.next is not None:
            heappush(minHeap, node.next) # needs to use def __lt__

    return resultHead


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    # expected output = [1, 2, 3, 3, 4, 6, 6, 7, 8]
    print("Here are the elements form the merged list: ")
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next

main()


# ----------Brute Force Solution----------
# A brute force solution could be to add all elements of the given ‘K’ lists to one list and sort it.
#   -> If there are a total of ‘N’ elements in all the input lists, 
#      then the brute force solution will have a time complexity of O(N*logN) to sort the merged list.
#   -> Can we do better than this? 
""" #   *** How can we utilize the fact that the input lists are individually sorted? """
# ----------Explanation----------
# If we have to find the smallest element of all the input lists, we have to compare only the smallest 
# (i.e. the first) element of all the lists. Once we have the smallest element, we can put it in the merged list. 
# Following a similar pattern, we can then find the next smallest element of all the lists to add it to the merged list.
""" # >>> The best data structure that comes to mind to find the smallest number among a set of ‘K’ numbers is a Heap. """
# ----------Steps for Algorithm----------
#    1.) We can insert the first element of each array in a Min-Heap.
#    2.) After this, we can take out the smallest (top) element from the heap and add it to the merged list.
#    3.) After removing the smallest element from the heap, we can insert the next element of the same list into the heap.
#    4.) We can repeat steps 2 and 3 to populate the merged list in sorted order.
