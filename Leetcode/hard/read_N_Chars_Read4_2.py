"""  ------- Read N Characters Given Read4 (2) - Call multiple times -------
Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. 
Your method read may be called multiple times.

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
    The read function may be called multiple times.
    Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
    You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
    It is guaranteed that in a given test case the same buffer buf is called by read.


Example 1:
Input: file = "abc", queries = [1,2,1]
Output: [1,2,0]
Explanation: The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.

Example 2:
Input: file = "abc", queries = [4,1]
Output: [3,0]
Explanation: The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0. """
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

from collections import deque

class Solution:
    def __init__(self):
            self.queue = deque()
            
    def read(self, buf: List[str], n: int) -> int:
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        read_chars, amount_left = 0, n

        while amount_left > 0:
            buf4 = [""] * 4
            read4(buf4)
            [self.queue.append(char) for char in buf4]
            if not self.queue:
                break
            while amount_left > 0 and self.queue:
                buf[read_chars] = self.queue.popleft()
                read_chars += 1
                amount_left -= 1
        
        return read_chars
        # Time: O(N)
        # Space: O(N) for queue
        