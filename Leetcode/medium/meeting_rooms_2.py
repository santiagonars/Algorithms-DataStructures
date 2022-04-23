""" ------- Meeting Rooms II -------
Given an array of meeting time intervals `intervals` where intervals[i] = [starti, endi], 
>>> return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
    1 <= intervals.length <= 104
    0 <= starti < endi <= 106 """


""" # SOLUTION: Using a min-heap as a priority queue """
import heapq   

def minRooms(intervals):
    if not intervals:
        return 0
    free_rooms = [] # for the heap
    intervals.sort(key=lambda x: x[0])
    # give a room to the first meeting using the `end time` of meeting
    heapq.heappush(free_rooms, intervals[0][1]) 

    for i in intervals[1:]:
        if free_rooms[0] <= i[0]: #if meeting ends before next meeting
            heapq.heappop(free_rooms)
        heapq.heappush(free_rooms, i[1]) # allocated room with end time
    return len(free_rooms)
    # Time: O(NlogN) for sorting the intervals array
    #       O(NlogN) as for every meeting N, we could push / pop average case is logN
    # Space: O(N) for the min-heap

intervals = [[0,30],[5,10],[15,20]]
print(minRooms(intervals)) # expected output = 2

intervals = [[7,10],[2,4]]
print(minRooms(intervals)) # expected output = 1

intervals = [[6,15],[13,20],[6,17]]
print(minRooms(intervals)) # expected output = 3


""" SOLUTIION: Chronological Order """
def minMeetingRooms(intervals):
    pass



# intervals = [[0,30],[5,10],[15,20]]
# print(minMeetingRooms(intervals)) # expected output = 2

# intervals = [[7,10],[2,4]]
# print(minMeetingRooms(intervals)) # expected output = 1

# meeting_intervals = [[6,15],[13,20],[6,17]]
# print(minMeetingRooms(meeting_intervals)) # expected output = 3