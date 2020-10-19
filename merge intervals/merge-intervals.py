""" ----------Merge Intervals (medium)----------
Problem Statement #
>>> Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5]. 

Example 2:
Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
 
Example 3:
Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one. 
--------------------------------------------------------------------------------
Similar Problems # 
Problem 1: Given a set of intervals, find out if any two intervals overlap.
NOTE: This would follow the same approach except just returns a bool as 'True' if they overlap
Example:
Intervals: [[1,4], [2,5], [7,9]]
Output: true
Explanation: Intervals [1,4] and [2,5] overlap """
# NOTE: Time complexity => O(N*logN), where ‘N’ is the total number of intervals.
#                       => iterating intervals will take O(N) but sorting them will take O(N*logN)
# NOTE: Space complexity => O(N), for the list of merged intervals been returned

from __future__ import print_function # brings bring the print function from Python 3 into Python 2.6+


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    # if there is only 1 interview jsut return it
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time to ensure a.start <= b.start
    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end: # => they are overlapping intervals; change the 'end' for the highest one
            end = max(interval.end, end)
        else: # =>  non-overlapping intervals; add the previous interval and reset
            mergedIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    # add the last interval
    mergedIntervals.append(Interval(start, end))
    return mergedIntervals


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1,4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()  # expected output = [1, 5][7, 9]
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval() # expected output = [2, 4][5, 9]
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval() # expected output = [1, 6]
    print()


main()