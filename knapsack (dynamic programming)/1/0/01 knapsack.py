""" ----------0/1 Knapsack (medium)----------
Introduction #
>>> Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’ 
The goal is to get the maximum profit out of the knapsack items. 
Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. 
Here are the weights and profits of the fruits:
    Items: { Apple, Orange, Banana, Melon }
    Weights: { 2, 3, 1, 4 }
    Profits: { 4, 5, 3, 7 }
    Knapsack capacity: 5

Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:

    Apple + Orange (total weight 5) => 9 profit
    Apple + Banana (total weight 3) => 7 profit
    Orange + Banana (total weight 4) => 8 profit
    Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination as it gives us the maximum profit, and the total weight does not exceed the capacity.

Problem Statement #
>>> Given two integer arrays to represent weights and profits of ‘N’ items, 
we need to find a subset of these items which will give us maximum profit 
such that their cumulative weight is not more than a given number ‘C.’ 
Each item can only be selected once, which means either we put an item in the knapsack or we skip it. """


""" ------------brute-force solution------------ """
# Time Complexity: exponential O(2^N) ,where 'N' is the total number of items. There are a toral of 31 recursive calls for (2^N) + (2^N) - 1
# Space Complexity: O(N) ,used to store the recursion stack. We can't have more the 'N' recursive calls on the call stack at any time 
#                                                            since the recursive alogrithm works in a depth-first fashion.
def solve_knapsack_1(profits, weights, capacity):
    return knapsack_recursive_1(profits, weights, capacity, 0)


def knapsack_recursive_1(profits, weights, capacity, currentIndex):
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # recursive call, after selecting the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive_1(profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive_1(profits, weights, capacity, currentIndex + 1) 

    return max(profit1, profit2)

""" ------------Top-down Dynamic Programming with Memoization Solution------------
NOTE: We can use Memoization to solve overlapping sub-problems efficiently.
    - Memoization is when we store the results of all the previously solved sub-problems and 
        return the results from memory if we encounter a problem that has already been solved.
    * we can use a two-dimensional array to store the results of all the solved sub-problems. """

# Time Complexity: O(N*C) => where ‘N’ is the number of items and ‘C’ is the knapsack capacity. Since the memoization array dp[profits.length][capacity+1]
#                         => stores results for all subproblems, there can not be more than N * C subproblems.
# Space Complexity: O(N*C + N) => which is asymptotoically equivalent to O(N*C)
#                              => O(N) space to store the recusive stack + O(N*C) space for the memoization array
def solve_knapsack_2(profits, weights, capacity):
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive_2(dp, profits, weights, capacity, 0)


def knapsack_recursive_2(dp, profits, weights, capacity, currentIndex):
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    # recursive call, after selecting the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive_2(dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive_2(dp, profits, weights, capacity, currentIndex + 1) 

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]

"""  ------------Bottom-up Dynamic Programming Solution------------
Populate the dp[][] array from the above solution by working in a bottom-up fashion and 
find the maximum profit for every sub-array and every possible capacity.
* This means that dp[i][c] will represent the maximum knapsack profit for capacity ‘c’ calculated from the first ‘i’ items.

An optimal solution will be maximum of two values:

    dp[i][c] = max (dp[i-1][c], profit[i] + dp[i-1][c-weight[i]]) """

# Time Complexity: O(N*C) => where ‘N’ is the number of items and ‘C’ is the maximum capacity.
# Space Complexity: O(N*C) => where ‘N’ is the number of items and ‘C’ is the maximum capacity.
def solve_knapsack_3(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or  len(weights) != n:
        return 0

    dp = [[-1 for x in range(capacity+1)] for y in range(n)]

    # populate the capacity = columns, with '0' capacity we have '0' profits
    for i in range(0, n):
        dp[i][0] = 0

    # if we have only one weight, we willl take it as if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profits2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            # exclude the item
            profit2 = dp[i - 1][c]
            # take maximum
            dp[i][c] = max(profit1, profit2)

    print_selected_elements(dp, weights, profits, capacity)
    # maximum profit will be at the bottom-right corner
    return dp[n - 1][capacity]


def print_selected_elements(dp, weights, profits, capacity):
    print("Selected weights are: ", end='')
    n = len(weights)
    totalProfit = dp[n - 1][capacity]
    for i in range(n-1, 0, -1):
        if totalProfit != dp[i - 1][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            totalProfit -= profits[i]

    if totalProfit != 0:
        print(str(weights[0]) + " ", end='')
    print()


def main():
    # Brute-force solution
    print(solve_knapsack_1([1, 6, 10, 16], [1, 2, 3, 5], 7)) # expected = 22
    print(solve_knapsack_1([1, 6, 10, 16], [1, 2, 3, 5], 6)) # expected = 17
    print()
    # Top-down Dynamic Programming with Memoization solution
    print(solve_knapsack_2([1, 6, 10, 16], [1, 2, 3, 5], 7)) # expected = 22
    print(solve_knapsack_2([1, 6, 10, 16], [1, 2, 3, 5], 6)) # expected = 17
    print()
    # Bottom-up Dynamic Programming solution
    print(solve_knapsack_3([1, 6, 10, 16], [1, 2, 3, 5], 7)) # expected = 22
    print(solve_knapsack_3([1, 6, 10, 16], [1, 2, 3, 5], 6)) # expected = 17


main()
    

