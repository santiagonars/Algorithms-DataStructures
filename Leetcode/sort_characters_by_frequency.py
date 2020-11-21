""" ----------Sort Characters By Frequency----------
Problem:
>>> Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input: "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: "cccaaa"
Output: "cccaaa"
Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters. """
# Time complexity => O(N + NlogK)
# Time complexity => O(K + N)
from heapq import heappop, heappush


def sort_chars_by_frequency(strg):
    result = ""
    frequency_map = {} 
    minHeap = [] 

    # store frequency count in hashmap
    for char in strg:
        frequency_map[char] = frequency_map.get(char, 0) + 1
    
    # add to min-heap
    for char, frequency in frequency_map.items():
        heappush(minHeap, (frequency, char))

    while minHeap:
        (frequency, char) = heappop(minHeap)
        result = (char * frequency) + result

    return result


def main():
    s = "tree"
    print(sort_chars_by_frequency(s)) # expected = "eert"
    s = "cccaaa"
    print(sort_chars_by_frequency(s)) # expected = "cccaaa"
    s = "Aabb"
    print(sort_chars_by_frequency(s)) # expected = "bbaA"

main()


"""
Constraints:
- all chars need to be group together
- case sensitive

Q's to ask:
- In the input string, are there any leading or trailing spaces?
    -> NOTE: use lstrip() for leading; rstrip() for trailing; strip() for both
- In the input string, are there any spaces in between?
    -> NOTE: use string_noSpaces = "".join(string.split()) to remove spaces

TODO: 
- CREATE a hashmap, a heap, and a result string

- add chars to hashmap with frequency count as the value

- for loop hashmap.items:
    push each (frequency, char) as tuple to the min-heap

- while heap is not empty
    smallest_frequecy = pop value from top of the heap (smallest value)
    position = len(result)
    result = result[:position] + (smallest_frequecy * hashmap[smallest_frequecy])

>>> Time Complexity: O(N + K*logK + logK) = O(N + NlogK) , where 'N' is total number of characters, 'K' is total number unique characters
>>> Space Complexity: O(K + K + N) = O(K + N)
"""