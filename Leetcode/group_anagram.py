""" ----------Group Anagram (Medium)----------
Problem:
>>> Given an array of strings 'strs', group the anagrams together. You can return the answer in any order.

* An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""
# Time Complexity => O(N*KlogK) , for 'N' is the number of strings in 'strs' array & 'K' is the number of number of characters in the strings.
#                               , for loop is O(N) + to sort each 'N' string it takes O(KlogK), hence O(NKlogK)
# Space Complexity => O(N*K)
import collections


def groupAnagram(strs):
    result_map = collections.defaultdict(list)
    for s in strs:
        result_map[tuple(sorted(s))].append(s)

    # result = [i for i in result_map.values()] # => to return as a list dtype
    return result_map.values()


def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagram(strs)) # expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    strs = [""]
    print(groupAnagram(strs)) # expected = [""]
    strs = ["a"]
    print(groupAnagram(strs)) # expected = ["a"]


main()

