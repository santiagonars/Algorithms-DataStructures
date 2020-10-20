""" ----------Insert Interval (medium)----------
Problem Statement #
>>> Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and merge all necessary intervals 
to produce a list that has only mutually exclusive intervals.

Example 1:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Example 2:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Example 3:
Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4]. """
# NOTE: Time complexity => O(N), to iteration through the intervals once, where ‘N’ is the total number of intervals 
# NOTE: Space complexity => O(N), to return a list of the merged interval

def insert(intervals, new_interval):
    merged = []
    i = 0
    start, end = 0, 1

    # skip all intervals before the 'new_interval' (and add to output)
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    # merge all intervals that overlap with 'new_interval'
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1
    
    # insert the new_interval
    merged.append(new_interval)

    # add all the remaining intervals to the output
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


def main():
    # expected output = [[1,3], [4,7], [8,12]]
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    # expected output = [[1,3], [4,12]]
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    # expected output = [[1,4], [5,7]]
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()

# NOTE: Interval list is sorted so a better solution than using than the merged intervals solution which gave O(N*logN) can be used.
#
# 1) Skip all intervals which end before the start of the new interval, i.e., skip all intervals with the following condition:
#       =>       intervals[i].end < newInterval.start
# 2) Let’s call the last interval ‘b’ that does not satisfy the above condition. 
#    If ‘b’ overlaps with the new interval (a) (i.e. b.start <= a.end), we need to merge them into a new interval ‘c’:
#       =>       c.start = min(a.start, b.start)
#       =>       c.end = max(a.end, b.end)
# 3) We will repeat the above two steps to merge ‘c’ with the next overlapping interval.


