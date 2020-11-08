""" --------Sliding Window Median (hard)--------
Problem Statement #
>>> Given an array of numbers and a number ‘k’, 
find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:
Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0

Example 2:
Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0 """
# NOTE: Time complexity => O(N * K) ,where ‘N’ is the total number of elements in the input array 
#                       => and ‘K’ is the size of the sliding window. We have to go through all 'N' numbers while:
#                       =>  1.) Insert/remove numbers from heaps of size ‘K’. This will take O(logK)
#                       =>  2.) Remove the element going out of the sliding window which will take O(K)
#                       =>      to seach this element in a heap of size 'K'
# NOTE: Space complexity =>  O(K) ,ignoring the output array because all numbers stored in heaps are within the sliding window.

import heapq
from heapq import heappush, heappop, heapify
# from heapq import *

class SlidingWindowMedian:

    def __init__(self):
        self.maxHeap = [] # for the smallest numbers
        self.minHeap = [] # for the largest numbers

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums) - k + 1)] # number of k-subarrays in 'nums'
        for i in range(0, len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            self.rebalance_heaps()

            if i - k + 1 >= 0: # if there are at least 'k' elements in the sliding window
                # add the median to the the result array
                if len(self.maxHeap) == len(self.minHeap):
                    # we have even number of elements, take the average of middle two elements
                    result[i - k + 1] = -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
                else: # max-heap will have one more element than the min-heap
                    result[i - k + 1] = -self.maxHeap[0] / 1.0

                # remove the the element going out of the sliding window
                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elementToBeRemoved)
                else:
                    self.remove(self.minHeap, elementToBeRemoved)

                self.rebalance_heaps()

        return result
    
    def rebalance_heaps(self):
        # either both the heaps will have equal number of elements 
        # or max-heap will have one more element than the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap)) # move top element from max-heap to min-heap
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap)) # move top element from min-heap to max-heap

    # removes an element from the heap keeping the heap property
    def remove(self, heap, element):
        ind = heap.index(element) # find the element
        # move element to the end and delete it
        heap[ind] = heap[-1]
        del heap[-1]
        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will be O(logN)
        if ind < len(heap):
            heapq._siftup(heap, ind)  #????!
            heapq._siftdown(heap, 0, ind)
    
    # Alternative maybe
"""     def find_sliding_window_median_2(self, nums, k):
        result = []
        window_start = 0
        for window_end in range(len(nums)):
            # make window smaller if it's larger than k
            if window_end + 1 > k:
                # TODO: remove number at window_start from heap
                window_start += 1

            if not self.maxHeap or -self.maxHeap[0] >= nums[window_end]:
                heappush(self.maxHeap, -nums[window_end])
            else:
                heappush(self.minHeap, nums[window_end])

            # check that it is balanced
            # -> either is max-heap has just 1 more element than the min-heap or has same number of elements
            self.rebalance_heaps()
            # print("max: ", self.maxHeap)
            # print("min: ", self.minHeap)

            # get median
            if window_end - window_start + 1 >= k or len(nums) <= k:
                if len(self.maxHeap) == len(self.minHeap):
                    result.append(-self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0)
                else:
                    result.append(-self.maxHeap[0] / 1.0)     

        return result """

 
def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2) 
    print("Sliding window medians are: " + str(result)) # expected output = [1.5, 0.5, 1.0, 4.0]

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result)) # expected output = [1.0, 2.0, 3.0]


main()


