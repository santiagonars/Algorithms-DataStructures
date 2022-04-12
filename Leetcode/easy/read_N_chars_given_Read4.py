""" ------- Read N Characters Given Read4 -------
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

Method read4:
    The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.
    The return value is the number of actual characters read.
    Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

        Parameter:  char[] buf4
        Returns:    int

    buf4[] is a destination, not a source. The results from read4 will be copied to buf4[]. 

Method read:
    By using the read4 method, implement the method read that reads n characters from file and store it in the buffer array buf. Consider that you cannot manipulate file directly.
    The return value is the number of actual characters read.
    Definition of read:

        Parameters:	char[] buf, int n
        Returns:	int

    buf[] is a destination, not a source. You will need to write the results to buf[].

Note:
    Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
    The read function will only be called once for each test case.
    You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
 

Example 1:
Input: file = "abc", n = 4
Output: 3
Explanation: After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
Note that "abc" is the file's content, not buf. buf is the destination buffer that you will have to write the results to.

Example 2:
Input: file = "abcde", n = 5
Output: 5
Explanation: After calling your read method, buf should contain "abcde". We read a total of 5 characters from the file, so return 5.

Example 3:
Input: file = "abcdABCD1234", n = 12
Output: 12
Explanation: After calling your read method, buf should contain "abcdABCD1234". We read a total of 12 characters from the file, so return 12."""


# See link:
# https://leetcode.com/problems/read-n-characters-given-read4/solution/


class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copied_chars = 0
        read_chars = 4
        buf4 = [''] * 4
        
        while copied_chars < n and read_chars == 4:
            read_chars = read4(buf4) # only call this as long as `read_chars`  keeps getting reading 4 characters, so file could be still be longer
        
            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i] # update buf from buf4
                copied_chars += 1
        
        return copied_chars
        # Time: O(N)
        # Space: O(1)