"""  ------- Paint Fence -------
You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.

>>> There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.

Example 1:
Input: n = 3, k = 2
Output: 6
Explanation: All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.

Example 2:
Input: n = 1, k = 1
Output: 1

Example 3:
Input: n = 7, k = 2
Output: 42

Constraints:
    1 <= n <= 50
    1 <= k <= 105
    The testcases are generated such that the answer is in the range [0, 231 - 1] for the given n and k. """

""" ----- SOLUTION: To-Down Dynamic Programming (Recursion + Memoization) -----
>>> Typically implemeted with recursion and made more efficient with memoization """
from functools import lru_cache
def numWays(n, k):
    @lru_cache(None) # wrapper to automatically memoize a function
    def totalWays(i):
        if i == 1:
            return k
        if i == 2:
            return k * k

        if i in memo:
            return memo[i]

        memo[i] = (k - 1)*(totalWays(i - 1) + totalWays(i - 2))
        return memo[i]
    memo = {}
    return totalWays(n)
    # Time: O(N) totalWays gets called from n to 3 for each index, but with 
    # Space: O(N) for the recursion call O(N) stack and the hashmap O(N - 2)

n = 3
k = 2
print(numWays(n, k)) # expect: 6

n = 1
k = 1
print(numWays(n, k)) # expect: 1

n = 7
k = 2
print(numWays(n, k)) # expect: 42


""" ----- SOLUTION: Bottom-Up Dynamic Programming (Tabulation) -----
>>> Known as tabulation and is done iteratively
use a totalWays array instead and totalWays[i] represent the number of ways to paint i fence posts """
def numWays_bottomUp(n, k):  
    if n == 1:
        return k
    if n == 2:
        return k * k

    total_ways = [0] * (n + 1)
    total_ways[1] = k
    total_ways[2] = k * k

    for i in range(3, n + 1):
        total_ways[i] = (k - 1) * (total_ways[i - 1] + total_ways[i - 2])

    return total_ways[n]
    # Time: O(N) need to iterate from 3 to n
    # Space: O(N) for array `total_ways` that has a length of n + 1

print("-"*10)
n = 3
k = 2
print(numWays_bottomUp(n, k)) # expect: 6

n = 1
k = 1
print(numWays_bottomUp(n, k)) # expect: 1

n = 7
k = 2
print(numWays_bottomUp(n, k)) # expect: 42










