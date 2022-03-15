'''
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length'''
# NOTE: similar to a longest subarray problem

def totalFruits(fruits):
    max_number_fruit = 0
    window_start = 0
    fruit_count_map = {} 

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]

        if right_fruit not in fruit_count_map:
            fruit_count_map[right_fruit] = 0
        fruit_count_map[right_fruit] += 1

        while len(fruit_count_map) > 2: #length number of unique fruits must 2
            left_fruit = fruits[window_start]
            fruit_count_map[left_fruit] -= 1

            if fruit_count_map[left_fruit] == 0:
                del fruit_count_map[left_fruit]
            window_start += 1

        max_number_fruit = max(max_number_fruit, window_end - window_start + 1)
    return max_number_fruit


fruits = [1,2,1] #output = 3
result = totalFruits(fruits)
print(result)

# fruits = [0,1,2,2] #output = 3
result = totalFruits(fruits)
print(result)

fruits = [1,2,3,2,2] #output = 4
result = totalFruits(fruits)
print(result)
