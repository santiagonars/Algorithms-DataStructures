""" ----------Problem Statement----------
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, 
find the length of the longest substring having the same letters after replacement.

Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc". """
# NOTE: Time complexity => O(N) => for N  is the number of letters int the string to traverse
# NOTE:  Space complexity => O(1) => constant space for hashmap will store up to 26 letters, hence O(26)


def length_of_longest_substring(string, k):
    max_length = 0 
    window_start = 0
    max_repeat_letter_count = 0 
    letter_frequency_map = {} 
    
    for window_end in range(len(string)): 
        right_char = string[window_end] # get next character and add to dictionary
        if right_char not in letter_frequency_map:
            letter_frequency_map[right_char] = 0
        letter_frequency_map[right_char] += 1
        # get letter count of the letter of each iteration to suntract from window size
        max_repeat_letter_count = max(max_repeat_letter_count, letter_frequency_map[right_char])
        # window size cannot have more than k letters after subtracting 'max_repeat_letter_count' of the letter of each iteration
        # ^if so, make window size smaller
        if (window_end - window_start + 1 - max_repeat_letter_count)  > k:
            left_char = string[window_start]
            letter_frequency_map[left_char] -= 1
            window_start += 1 

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == "__main__":
    string_test1 = "aabccbb"
    k = 2
    print("Length of the longest substring: ", length_of_longest_substring(string_test1, k)) # expected output = 5
    string_test2 = "abbcb"
    k = 1
    print("Length of the longest substring: ", length_of_longest_substring(string_test2, k)) # expected output = 4
    string_test3 = "abccde"
    k = 1
    print("Length of the longest substring: ", length_of_longest_substring(string_test3, k)) # expected output = 3
