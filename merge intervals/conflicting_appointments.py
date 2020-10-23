""" ----------Conflicting Appointments (medium)----------
Problem Statement #
>>> Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:
Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Example 2:
Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Example 3:
Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments. 
----------------------------------------------------------------------------------------------
Similar Problems #
Problem : Given a list of appointments, find all the conflicting appointments.
NOTE: In this case it can be solved the same way except create and return a result list for conflicting appoinments.
Example:
Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
Output: 
[4,5] and [3,6] conflict. 
[3,6] and [5,7] conflict. """
# NOTE: Time complexity => O(N*logN), because we need to sort the appointments
# NOTE: Space complexity => O(N), needed for sorting


def can_attend_all_appointments(intervals):
    # sort by the first postion of each appointmnet in the intervals list
    intervals.sort(key=lambda x: x[0])
    start, end =  0, 1

    for i in range(1, len(intervals)):
        # If the previous appointment ends after the next appointment, they overlap
        # NOTE: Here is they previous appointment ends at the same time (=), 
        # -> then they don't overlap because one starts right after the other
        if intervals[i][start] < intervals[i-1][end]:
            return False
    return True

def main():
    # expected output = False
    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    # expected output = True
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    # expected output = False
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()


# NOTE: The problem follows the Merge Intervals pattern. 
# 1) Sort all the intervals by start time.
# 2) Then check if any two intervals overlap, return false.
#   => A person will not be able to attend all appointments if any two appointments overlap, 