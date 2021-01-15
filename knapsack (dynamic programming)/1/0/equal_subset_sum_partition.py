""" ----------Equal Subset Sum Partition (medium)----------
Problem Statement #
>>> Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Example 1:
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

Example 2:
Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}

Example 3:
Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum. """

# NOTE: BASE SOLUTION ALGORITHM:
# 1+2+3+4 = 10 = total sum = S; hence need to find a subset that equals S/2
# find S/2
# for each number 'i'
#     create a new set which INCLUDES number 'i' if it does not exceed 'S/2', and recursively process the remaining numbers
#     create a new set WITHOUT number 'i', and recursively process the remaining items
# return true if any of the above sets has a sum equal to 'S/2', otherwise return false
# 

""" # ------------BRUTE-FORCE SOLUTION------------ """
# Time complexity: O(2^N) ,where ‘N’ represents the total number.
# Space complexity: O(N) to store the recursion stack.
def can_partition_1(num):
    s = sum(num) # time complexity of sum() is O(N)
    if s % 2 != 0: # if the total sum is odd, the sum of the subset cannot be equal as they are intergers
        return False
    return can_partition_recursive_1(num, s / 2, 0)


def can_partition_recursive_1(num, sum, currentIndex):
    # base check
    if sum == 0:
        return True

    n = len(num)
    if n == 0 or currentIndex >= n:
        return False

    # recursive call after choosing the number at the `currentIndex`
    # if the number at `currentIndex` exceeds the sum, we shouldn't process this
    if num[currentIndex] <= sum:
        if (can_partition_recursive_1(num, sum - num[currentIndex], currentIndex + 1)):
            return True

    # recursive call after excluding the number at the 'currentIndex'
    return can_partition_recursive_1(num, sum, currentIndex + 1)


""" # ------------TOP-DOWN DYNAMIC PROGRAMMING WITH MEMOIZATION SOLUTION------------ """
# Memoization is when we store the results of all the previously solved sub-problems so we can return the results 
#              from memory if we encounter a problem that has already been solved
# Use a two-dimensional array to store the results for every subset and for every possible sum.
#   - The first dimension of the array will represent different subsets
#   - The second dimension will represent different ‘sums’ that we can calculate from each subset.

# Time complexity: O(N * S) ,where ‘N’ represents the total number of subsets and 'S' is the total sum of all the numbers
# Space complexity: O(N * S) for the two-dimensional memoizationnarray + O(N) to store the recursion stack.
def can_partition_2(num):
    s = sum(num) 
    # 's' cannot be an odd number as two subsets can not equal the total sum
    if s % 2 != 0: 
        return False

    # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
    dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(num))]
    return True if can_partition_recursive_2(dp, num, int(s / 2), 0) == 1 else False


def can_partition_recursive_2(dp, num, sum, currentIndex):
    # base check
    if sum == 0:
        return 1

    n = len(num)
    if n == 0 or currentIndex >= n:
        return 0

    # if we have not already processed a similar problem
    if dp[currentIndex][sum]== -1:
        # recursive call: INCLUDING the number at the `currentIndex` 
        # if the number at `currentIndex` exceeds the sum, we shouldn't process this
        if num[currentIndex] <= sum:
            if (can_partition_recursive_2(dp, num, sum - num[currentIndex], currentIndex + 1)):
                dp[currentIndex][sum] = 1
                return 1
        
        # recursive call: EXCLUDING the number at the 'currentIndex'
        dp[currentIndex][sum] = can_partition_recursive_2(dp, num, sum, currentIndex + 1)

    return dp[currentIndex][sum]

""" # ------------BOTTOM-UP DYNAMIC PROGRAMMING SOLUTION------------ """
# We want to find if we can make all possible sums with every subset.
# dp[i][s] will be ‘true’ if we can make the sum ‘s’ from the first ‘i’ numbers.
# 
# So, for each number at index ‘i’ (0 <= i < num.length) and sum ‘s’ (0 <= s <= S/2), we have two options:
#    1) Exclude the number. 
#          -> In this case, we will see if we can get ‘s’ from the subset excluding this number: dp[i-1][s]
#    2) Include the number if its value is not more than ‘s’. 
#          -> In this case, we will see if we can find a subset to get the remaining sum: dp[i-1][s-num[i]]

# Time complexity: O(N * S) ,where ‘N’ represents the total number of subsets and 'S' is the total sum of all the numbers
# Space complexity: O(N * S)
def can_partition_3(num):
    s = sum(num)

    # if 's' is a an odd number, we can't have two subsets with same total
    if s % 2 != 0:
        return False

    # we are trying to find a subset of given numbers that has a total sum of 's/2'.
    s = int(s / 2)

    n = len(num)
    dp = [[False for x in range(s+1)] for y in range(n)]

    # populate the s=0 columns, as '0' sum  can always  be found with an empty set
    for i in range(n):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is equal to its value
    for j in range(1, s+1):
        dp[0][j] = num[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, s+1):
            # if we can get the sum 'j' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]: # else if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - num[i]]
    # the bottom-right corner will have our answer.
    return dp[n - 1][s]


def main():
    # brute-force
    s = [1, 2, 3, 4]
    print(can_partition_1(s)) # expect = True
    s = [1, 1, 3, 4, 7]
    print(can_partition_1(s)) # expect = True
    s = [2, 3, 4, 6]
    print(can_partition_1(s)) # expect = False
    print()
    # top-down dynamic programming with memoization
    s = [1, 2, 3, 4]
    print(can_partition_2(s)) # expect = True
    s = [1, 1, 3, 4, 7]
    print(can_partition_2(s)) # expect = True
    s = [2, 3, 4, 6]
    print(can_partition_2(s)) # expect = False
    print()
    # bottom-up dynamioc programming with memoization
    s = [1, 2, 3, 4]
    print(can_partition_3(s)) # expect = True
    s = [1, 1, 3, 4, 7]
    print(can_partition_3(s)) # expect = True
    s = [2, 3, 4, 6]
    print(can_partition_3(s)) # expect = False


main()