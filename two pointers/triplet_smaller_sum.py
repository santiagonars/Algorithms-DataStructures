""" Triplets with Smaller Sum (medium)
Problem Statement #
>>> Given an array 'arr' of unsorted numbers and a target sum, 
count all triplets in it such that 'arr[i] + arr[j] + arr[k] < target' where i, j, and k are three different indices. 
Write a function to return the count of such triplets.

Example 1:
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Example 2:
Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3] 
#----------------------------------------------------------------------------------------------
Similar Problems #
>>> Problem: Write a function to return the list of all such triplets instead of the count. 
How will the time complexity change in this case?

Solution: Following a similar approach we can create a list containing all the triplets. 
          *** only the lines with the comment "# NOTE: changed" have changed: """
# NOTE: Time complexity => O(N^2) => sorting is O(N * logN). searchPair() is O(N).
#                                 => searchTriplets() will take O(N * logN + N^2) = O(N^2)
# NOTE: Space complexity => O(N) ,for sorting


def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()
    for i in range(len(arr)):
        count += search_pair(arr, target - arr[i], i)
    return count


def search_pair(arr, target_sum, first):
    count = 0
    left = first + 1
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target_sum: # triplet found
            # any value after left up to right in arr[right] will also be less than the target sum
            # since the array si sorted we know that arr[right] >= arr[left]
            count += right - left 
            left += 1
        else:
            right -= 1 # need a pair with a smaller sum

    return count

# similar problem, instead it returns a list of the triplets instead of the count
def triplet_with_smaller_sum_2(arr, target):
    arr.sort()
    triplets = [] # NOTE: changed
    for i in range(len(arr)-2):
        search_pair_2(arr, target - arr[i], i, triplets)
    return triplets # NOTE: changed


def search_pair_2(arr, target_sum, first, triplets):
    left = first + 1
    right = len(arr) - 1
    while (left < right):
        if arr[left] + arr[right] < target_sum:  # # triplet found
            # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
            # left and right to get a sum less than the target sum
            for i in range(right, left, -1): # NOTE: changed ; decrement by 1 from positive to negative
                triplets.append([arr[first], arr[left], arr[i]]) # NOTE: changed
            left += 1 
        else:
            right -= 1  # we need a pair with a smaller sum


def main():
    # print(triplet_with_smaller_sum([-1, 0, 2, 3], 3)) # expected output = 2
    # print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5)) # expected output = 4
    # expected output = [[-1, 0, 3], [-1, 0, 2]]
    print(triplet_with_smaller_sum_2([-1, 0, 2, 3], 3)) 
    # expected output = [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]
    print(triplet_with_smaller_sum_2([-1, 4, 2, 1, 3], 5))


main()


# NOTE: sort the array and then iterate through it, taking one number at a time. 
# Let’s say during our iteration we are at number ‘X’, 
# so we need to find ‘Y’ and ‘Z’ such that X + Y + Z < target. 
# At this stage, our problem translates into finding a pair whose sum is less than “target - X” 
# (as from the above equation Y + Z == target - X)