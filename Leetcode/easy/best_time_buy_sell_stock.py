""" ------- Best Time to Buy and Sell Stock -------
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

>>> Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104 """

""" ----- SOLUTION: Brute Force ----- """
def maxProfit_Brute(prices):
    max_profit = 0

    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            temp = prices[j] - prices[i]
            max_profit = max(max_profit, temp)

    return max_profit
    # Time: O(N ^ 2)
    # Space: O(1)

# prices = [7,1,5,3,6,4]
# print(maxProfit_Brute(prices)) # expect: 5

# prices = [7,6,4,3,1]
# print(maxProfit_Brute(prices)) # expect: 0

""" ----- SOLUTION: Optimized (FASTEST) ----- """
def maxProfit_Optimized(prices):
    lowest_purchase = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        temp = prices[i] - lowest_purchase

        if temp > max_profit:
            max_profit = temp
            
        if prices[i] < lowest_purchase:
            lowest_purchase = prices[i]

    return max_profit
    # O(N) time
    # O(N) space

# prices = [7,1,5,3,6,4]
# print(maxProfit_Optimized(prices)) # expect: 5

# prices = [7,6,4,3,1]
# print(maxProfit_Optimized(prices)) # expect: 0

""" ----- SOLUTION: Dynamic Programming (Tabulation) ----- """
def maxProfit(prices):
    n = len(prices)
    tab = [0] * n
    tab[0] = (prices[0], 0) # [lowest price, max profit] initial values
    min_price = max_profit = 0

    for i in range(1, n):
        min_price = min(tab[i-1][0], prices[i]) # either previous lowest price or current
        max_profit = max(tab[i-1][1], prices[i]-tab[i-1][0]) # either previous max_profit or current profit

        tab[i] = (min_price, max_profit)

    return tab[n - 1][1]
    # O(N) time
    # O(N) space


prices = [7,1,5,3,6,4]
print(maxProfit(prices)) # expect: 5

prices = [7,6,4,3,1]
print(maxProfit(prices)) # expect: 0