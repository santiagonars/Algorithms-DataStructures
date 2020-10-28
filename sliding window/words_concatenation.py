""" ----------Problem Challenge 4---------- 
>>> --------Words Concatenation (hard)---------
Given a string and a list of words, find all the starting indices of substrings in the given string that are a 
`concatenation of all the given words` exactly once without any overlapping of words. 
***It is given that all words are of the same length.

Example 1:
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:
Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox". """
# NOTE: Time complexity => O(N * M * Len) ,where ‘N’ is the number of characters in the given string, 
#                       =>‘M’ is the total number of words, and ‘Len’ is the length of a word.
# NOTE: Space complexity => O(M + N) ,at worse to store all the words in the two HashMaps need O(M),
#                        => and O(N) space for the resulting list

def find_word_concatenation(string, words):
    result_indices = []
    word_frequency = {}

    # if the 'words' input is empty
    if len(words) == 0  or len(words[0]) == 0:
        return result_indices
    
    for word in words:
        if word not in word_frequency.keys():
            word_frequency[word] = 0
        word_frequency[word] += 1

    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(string) - words_count * word_length) + 1):
        words_seen = {}
        
        for j in range(0, words_count):
            next_word_index = i + j * word_length

            # Get the next word from the string
            word = string[next_word_index: next_word_index + word_length]
            if word not in word_frequency: 
                break # this means this word is not needed

            # Add the word to the 'words_seen' map
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # No need to process further if the word has higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0): # 'return 0 if key doesn't exist
                break
            
            # Store index if all the words are found (If this point all words have appeared in the string)
            if j + 1 == words_count:
                result_indices.append(i)

    return result_indices


if __name__ == "__main__":
    string_test = "catfoxcat"
    words = ["cat", "fox"]
    print(find_word_concatenation(string_test, words)) # expected output = [0, 3]
    string_test = "catcatfoxfox"
    words = ["cat", "fox"]
    print(find_word_concatenation(string_test, words))  # expected output = [3]


# NOTE: return list starting indices in string of the words concatenated together in any order
# >>> keep track of all the words in a HashMap and try to match them in the given string. 
# - Here are the set of steps for our algorithm:
#    1) Keep the frequency of every word in a HashMap.
#    2) Starting from every index in the string, try to match all the words.
#    3) In each iteration, keep track of all the words that we have already seen in another HashMap.
#    4) If a word is not found or has a higher frequency than required, we can move on to the next character in the string.
#    5) Store the index if we have found all the words.