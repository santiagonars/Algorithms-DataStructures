""" ----------Merge Sorted Array----------
Problem:
>>> Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively. 

*You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
*** Do not return anything, modify nums1 in-place instead.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[i] <= 109 """

def merge():
    pass


def main():
    # example 1
    nums1, m = [1,2,3,0,0,0], 3
    nums2, n = [2,5,6], 3
    merge(nums1, nums2) # expect = [1,2,2,3,5,6]
    # example 2
    nums1, m = [1], 1
    nums2, n = [], 0
    merge(nums1, nums2) # expect = [1]
    

