""" --------Find the Median of a Number Stream (medium)--------
Problem Statement #
>>> Design a class to calculate the median of a number stream. 
The class should have the following two methods:

    1.) insertNum(int num): stores the number in the class
    2.) findMedian(): returns the median of all numbers inserted in the class

*** If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
*** NOTE: numbers stay sorted in value

Example 1:
1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5 """
# NOTE: Time complexity => O(logN) for insertNum() => bc insertion for a heap is O(logN)
#                       => O(1) for findMedium() => elements at at the top of the heap
# NOTE: Space complexity => O(N) for storing all the numbers

from heapq import *


class MedianOfAStream:

    # NOTE: max-heap in Python have inverted values hence a value is pushed/popped a negative sign
    maxHeap = [] # first half of numbers
    minHeap = [] # second half of numbers

    def insert_num(self, num):
        # true when empty OR if 'num' is less than/equal to top element in max-heap
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num) # num is pushed inverted (with a negatice sign)
        else:
            heappush(self.minHeap, num)
        
        # REBALANCING STEP: either both heaps will have equal number of elements 
        # or max-heap will have one more element than the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1: # here max-heap has 2 or more elements than min-heaps
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap): # here min-heap has more elements
            heappush(self.maxHeap, -heappop(self.minHeap))
    
    def find_medium(self):
        if len(self.maxHeap) == len(self.minHeap):
            # we have even number of elements, take the average of middle two elements
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

        # because max-heap will have one more element than the min-heap
        return -self.maxHeap[0] / 1.0


def main():
    mediumOfAstream = MedianOfAStream()
    mediumOfAstream.insert_num(3)
    mediumOfAstream.insert_num(1)
    print("The median is: " + str(mediumOfAstream.find_medium())) # expected output = 2
    mediumOfAstream.insert_num(5)
    print("The median is: " + str(mediumOfAstream.find_medium())) # expected output = 3
    mediumOfAstream.insert_num(4)
    print("The median is: " + str(mediumOfAstream.find_medium())) # expected output = 3.5


main()


