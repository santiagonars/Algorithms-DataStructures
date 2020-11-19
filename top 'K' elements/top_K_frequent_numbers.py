""" --------Top 'K' Frequent Numbers (medium)--------
Problem Statement #
>>> Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once. """
# NOTE: Time complexity => O(N + N*logK) ,to add the numbers in the hashmap and then iterate through all value in hashmap
# NOTE: Space complexity => O(N) , to store all the numbers in the frequency hashmap

from heapq import *  # from heapq import heappush, heappop


def find_k_frequent_numbers(nums, k):

    # find the frequency of each number
    numFrequencyMap = {}
    for num in nums:
        numFrequencyMap[num] = numFrequencyMap.get(num, 0) + 1 # dict.get(key, default=None)

    minHeap = []

    # go through all numbers of the numFrequencyMap and push them in the minHeap, which will have
    # top k frequent numbers. If the heap size is more than k, we remove the smallest(top) number
    for num, frequency in numFrequencyMap.items():
        heappush(minHeap, (frequency, num)) # adding a tuple in the heap
        if len(minHeap) > k:
            heappop(minHeap)

    # create a list of top k numbers
    topNumbers = []
    while minHeap:
        topNumbers.append(heappop(minHeap)[1]) # add the num in the heap which is in index 1 of the tuple

    return topNumbers


# ALTERNATIVE SOLUTION
def find_k_frequent_numbers_2(nums, k):
    topNumbers = []
    num_freq = {}

    # add frequency count in hash map of all numbers
    for num in nums:
        if num not in num_freq:
            num_freq[num] = 0
        num_freq[num] += 1

    # first add up to k numbers in the heap
    for i in range(k):
        heappush(topNumbers, nums[i])

    # check hashmap if the remainding numbers in 'nums' appear more frequently
    for i in range(k, len(nums)):

        if num_freq[nums[i]] > num_freq[topNumbers[0]]:
            heappop(topNumbers)
            heappush(topNumbers, nums[i])

    return list(topNumbers)


def main():
    # expected output = [12, 11]
    print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))
    # expected output = [11, 5] or [11, 12] or [11, 3]
    print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))

    # expected output = [12, 11]
    print("Here are the K frequent numbers (ALTERNATIVE): " + str(find_k_frequent_numbers_2([1, 3, 5, 12, 11, 12, 11], 2)))
    # expected output = [11, 5] or [11, 12] or [11, 3]
    print("Here are the K frequent numbers (ALTERNATIVE): " + str(find_k_frequent_numbers_2([5, 12, 11, 3, 11], 2)))


main()

