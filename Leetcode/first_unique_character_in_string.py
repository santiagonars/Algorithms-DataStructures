""" ----------First Unique Character in a String----------
Problem:
>>> Given a string, find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1.

Examples 1:
s = "leetcode"
return 0.

Examples 2:
s = "loveleetcode"
return 2. 

Note: You may assume the string contains only lowercase English letters."""
# Time complexity => O(N) ,where it's actually O(2N) or O(N + N) to traverse once add characters in dictionary and 2nd time to check dictionary
# Space complexity => O(N) ,to save the values in the dictionary (hashmap)


def first_unique_character(string):
    """ 
    :type string: str
    """
    char_frequency = {}
    # add characters to hashmap
    for index in range(len(string)):
        char = string[index]
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    # check hashmap for index of first character with frequency count value of 1
    for index in range(len(string)):
        char = string[index]
        if char_frequency[char] == 1:
            return index

    return -1


def main():
    s = "leetcode"
    print(first_unique_character(s)) # expected output = 0
    s = "loveleetcode"
    print(first_unique_character(s)) # expected output = 2


main()



