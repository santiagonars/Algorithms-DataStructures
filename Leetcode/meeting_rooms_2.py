""" ----------Meeting Rooms II----------
>>> Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1 """
# Time complexity => O(N*LogN) for sorting
# Space complexity => O(N) sortng as well

"""
rooms_need = 0
i = 1
- Sort by the start of each apptment [0]
- create a start and end variable
if len(intervals) = 0: return rooms_need
if len(intervals) = 1: return rooms_need + 1
for loop in the range of the length of intervals
    room = 1
    j = 0
    while loop as long as current[i][ends] > next[i+j][starts]:
        rooms++
        j++
    rooms_need = max(max_rooms, rooms)
return rooms_need

>>> Time complexity: O(N*LogN) for sorting
>>> Space complexity: O(N)  ,space needed for sorting
"""
import heapq
# from heapq import heappush, heappop


# Solution using a priority queue (min-heap)
def minMeetingRooms(intervals):

    if not intervals:
            return 0
    
    # heap to track free rooms (by end time)
    free_rooms = []

    intervals.sort(key= lambda x: x[0])

    # Add a new room to the first meeting; add the end time 
    heapq.heappush(free_rooms, intervals[0][1])

    # Ggo through remanining meetins
    for i in intervals[1:]:
        # if the end time of the room is less than the start time, room is not needed anymore
        if free_rooms[0] <= i[0]: 
                heapq.heappop(free_rooms)

        heapq.heappush(free_rooms, i[1])

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)





# BUG: for other test cases: they appear on leetcode
def minMeetingRooms_2(intervals):
    """ 
    :intervals: list of list of intergers
    :return: returns min_rooms_needed 
    :return type: int
    """
    min_rooms_needed = 0
    intervals.sort(key=lambda x: x[0])

    start, end = 0, 1 # start and end of appointments

    if len(intervals) == 0: return min_rooms_needed
    if len(intervals) == 1: return min_rooms_needed + 1

    for i in range(1, len(intervals)): 
        room = 1
        j = 0
        while intervals[i - 1 + j][end] > intervals[i + j][start]:
            room += 1
            j += 1
            if i + j >= len(intervals) - 1:
                break
        # keep track of most rooms needed to accommodate meetings
        min_rooms_needed = max(min_rooms_needed, room)

    return min_rooms_needed


def main():
    meeting_intervals = [[0, 30],[5, 10],[15, 20]]
    print(minMeetingRooms(meeting_intervals)) # expected output = 2
    meeting_intervals = [[7,10],[2,4]]
    print(minMeetingRooms(meeting_intervals)) # expected output = 1
    meeting_intervals = [[6,15],[13,20],[6,17]]
    print(minMeetingRooms(meeting_intervals)) # expected output = 3

main()