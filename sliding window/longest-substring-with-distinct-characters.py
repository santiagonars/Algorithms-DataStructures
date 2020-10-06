""" ----------Problem Statement----------
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi". """
# NOTE: Time complexity => O(N) => same as O(N+N) asymptotically equivalent to O(N) because 
#                          The outer for loop runs for all characters 
#                          and the inner while loop processes each character only once.
# NOTE: Space complexity => O(K) => will be storing a maximum of ‘K+1’ characters in the HashMap.

def longest_substring_with_k_distinct(string, k):
    max_length = 0
    window_start = 0
    char_frequency = {}

    for window_end in range(len(string)):
        right_char = string[window_end]
        # insert characters in the hashmap with account value
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        # Once the number of distict charaters in the hashmap is greater than K, reduce it by
        # shrinking window until there are k distict characters in the 'char_frequency'
        while len(char_frequency) > k:
            left_char = string[window_start] # get character from left end and remove it from hashmap
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        # get maximum length with number of characters in window size with k distinct characters
        max_length = max(max_length, window_end - window_start + 1)  
    return max_length

if __name__ == "__main__":
    input_string_test1 = "araaci"
    k = 2
    print("Length of the longest substring: ", longest_substring_with_k_distinct(input_string_test1, k)) # expected output = 4
    input_string_test2 = "araaci"
    k = 1
    print("Length of the longest substring: ", longest_substring_with_k_distinct(input_string_test2, k)) # expected output = 2
    input_string_test3 = "cbbebi"
    k = 3
    print("Length of the longest substring: ", longest_substring_with_k_distinct(input_string_test3, k)) # expected output = 5