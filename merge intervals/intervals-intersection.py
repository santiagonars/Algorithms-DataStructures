""" ----------Intervals Intersection (medium)----------
Problem Statement #
>>> Given two lists of intervals, find the intersection of these two lists. 
Each list consists of disjoint intervals sorted on their start time.

Example 1:
Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6 ], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Example 2:
Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists. """
# NOTE: Time complexity => O(N+M), where ‘N’ and ‘M’ are the total number of intervals in the input arrays respectively.
# NOTE: Space complexity => O(1), it is constant time ignoring the result array but O(N) including it

# NOTE: The algorithm will be to iterate through both the lists together to see if any two intervals overlap. 
# If two intervals overlap, we will insert the overlapped part into a result list 
# and move on to the next interval which is finishing early.
# ***REMEMBER: Only returns common internals! If they dont interlap, do not add to output.

def merge(intervals_a, intervals_b):
    result = []
    i, j = 0, 0
    start, end = 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        # check if intervals overlap and intervals_a[i]'s start time lies within the other intervals_b[j]
        # => True if 'a' start greater than or equal to the start of 'b' and also less than or equal to the end of 'b'
        a_overlaps_b = intervals_a[i][start] >= intervals_b[j][start] and \
                        intervals_a[i][start] <= intervals_b[j][end]

        # check if intervals overlap and intervals_a[j]'s start time lies within the other intervals_b[i]
        # => True if 'b' start greater than or equal to start of 'a' and also less than or equal to end of 'a'
        b_overlaps_a = intervals_b[j][start] >= intervals_a[i][start] and intervals_b[j][start] >= intervals_a[i][end]

        # store the the intersection part
        if (a_overlaps_b or b_overlaps_a):
            result.append([max(intervals_a[i][start], intervals_b[j][start]), min(intervals_a[i][end], intervals_b[j][end])])

        # move next from the interval which is finishing first
        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return result


def main():
    # expected output = [2, 3], [5, 6 ], [7, 7]
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    # expected output = [5, 7], [9, 10] 
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))

main()