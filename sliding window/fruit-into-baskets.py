""" ----------Problem Statement----------
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits in each basket.
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

>>>Write a function to return the maximum number of fruits in both the baskets.

Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C'] """
# NOTE: Time complexity => O(N) => it is actually O(N+N) which is asymptotically equivalent to O(N)
#                          The outer for loop runs for all character and the inner while loop processes each character only once.
# NOTE: Space complexity => O(1) = > it's constant time bc it can be a mac of 3 types of fruits in frequency hashmap before it's removed

def fruits_into_baskets(fruits):
    max_number_fruits = 0
    window_start = 0
    fruit_baskets_frequency = {}

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        # add fruit to basket by unique fruit tree and keep a frequency count
        if right_fruit not in fruit_baskets_frequency:
            fruit_baskets_frequency[right_fruit] = 0
        fruit_baskets_frequency[right_fruit] += 1

        # shrink window until there are no more than 2 distict characters (or fruit types) in 'fruit_baskets_frequency' (or baskets)
        while len(fruit_baskets_frequency) > 2:
            left_fruit = fruits[window_start] 
            fruit_baskets_frequency[left_fruit] -= 1 # remove fruit from basket at the start of the window
            # remove fruit tree from basket if there aren't anymore for that type of fruit
            if fruit_baskets_frequency[left_fruit] == 0:
                del fruit_baskets_frequency[left_fruit]
            window_start += 1 # shrink sliding window
        # count number of fruits in the 2 baskets for 2 unique fruit trees; when length of 'fruit_baskets_frequency' is 2
        max_number_fruits = max(max_number_fruits, window_end - window_start + 1)
    return max_number_fruits


if __name__ == "__main__":
    fruits_arraytest1 = ['A', 'B', 'C', 'A', 'C']
    print("Maximum number of fruits: ", fruits_into_baskets(fruits_arraytest1)) # expected output = 3

    fruits_arraytest2 = ['A', 'B', 'C', 'B', 'B', 'C']
    print("Maximum number of fruits: ", fruits_into_baskets(fruits_arraytest2)) # expected output = 5