""" --------Top 'K' Numbers (easy)--------
Problem Statement #
>>> Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

Example 1:
Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]

Example 2:
Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12] """
# NOTE: Time complexity => O(N*logK) => The time complexity of this algorithm is O(K*logK+(N-K)*logK) 
#                                    => which asymptotically equivalent to O(N*logK)
# NOTE: Space complexity => O(K) to store the top ‘K’ numbers in the heap.


from heapq import * # need heappush, heappop


def find_k_largest_numbers(nums, k):
    minHeap = []
    # put first 'K' numbers in the min heap
    for i in range(k):
        heappush(minHeap, nums[i])

    # go through the remaining numbers of the array, if the number from the array is bigger than the
    # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return list(minHeap)


def main():
    # expected output = [5, 12, 11]
    print("Here are the top K numbers: " + str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))
    # expected output = [11, 12, 12]
    print("Here are the top K numbers: " + str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()

# NOTE: A brute force solution would sorting thew array which would give us O(NlogN)
#
# The best data structure that comes to mind to keep track of top ‘K’ elements is a Heap.
#
# >>> If we iterate through the array one element at a time and keep ‘K’ largest numbers in a heap 
# such that each time we find a larger number than the smallest number in the heap, we do two things:
#    1.) Take out the smallest number from the heap, and
#    2.) Insert the larger number into the heap.
#
# The most efficient way to repeatedly find the smallest number among a set of numbers will be to use a min-heap.
#    - finding smallest number in a min-heap in constant time O(1) since it's always at the root of the heap
#     - Extracting the smallest number from a min-heap will take O(logN)O(logN) (if the heap has ‘N’ elements) 
#       as the heap needs to readjust after the removal of an element.

# -------Steps for algorithm-------> given [3, 1, 5, 12, 2, 11], K = 3
#   1.) First, let’s insert ‘K’ elements in the min-heap.
#   2.) After the insertion, the heap will have three numbers [3, 1, 5] with ‘1’ being the root as it is the smallest element.
#   3.) We’ll iterate through the remaining numbers and 
#        perform the above-mentioned two steps if we find a number larger than the root of the heap.
#   4.) The 4th number is ‘12’ which is larger than the root (which is ‘1’), so let’s take out ‘1’ and insert ‘12’. 
#       Now the heap will have [3, 5, 12] with ‘3’ being the root as it is the smallest element.
#   5.) The 5th number is ‘2’ which is not bigger than the root of the heap (‘3’), 
#         so we can skip this as we already have top three numbers in the heap.
#   6.) The last number is ‘11’ which is bigger than the root (which is ‘3’), so let’s take out ‘3’ and insert ‘11’. 
#       Finally, the heap has the largest three numbers: [5, 12, 11]
#
# -------Time Complexity analysis-------
# It will take O(logK) to extract the minimum number from the min-heap. 
#   - It is O(logK), because we only need to store 'K' number of elements in the heap
# Overall time complexity of the algorithm will be O(K*logK + (N-K)*logK) since, first, 
#     we insert ‘K’ numbers in the heap and then iterate through the remaining numbers and at every step,
#    which in the worst case, we need to extract the minimum number and insert a new number in the heap. 
#       => This algorithm is better than O(N*logN).