""" ----------Valid Palindrome----------
Problem:
>>> Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
 
Constraints:
    s consists only of printable ASCII characters. """
# Time complexity => O(N)
# Space complexity => O(N)

# Solution #1 - using filter function
def isValidPalindrome(s):
    """ 
    :type s: str
    :rtype: bool
    """
    alphanumeric_filter = filter(str.isalnum, s) # get iterable of alphanumeric characters in `a_string`
    s = "". join(alphanumeric_filter).lower() # combine characters of `alphanumeric_filter` in a string
    
    return s == s[::-1]

# Solution #2 - using unicode values
def isPalindrome(s):
      """
      :type s: str
      :rtype: bool
      """
      x = ""
      diff = ord('a') - ord('A')
      for i in s:
        if ord(i)>=ord('a') and ord(i)<=ord('z') or ord(i)>=ord("0") and ord(i)<=ord("9"):
            x+=i
        elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
            i = chr(diff+ord(i))
            x+=i

      return x == x[::-1]


if __name__ == "__main__":
    # Solution #1
    print(isValidPalindrome("A man, a plan, a canal: Panama")) # expected output = True
    print(isValidPalindrome("race a car")) # expected output = False
    # Solution #2
    print(isPalindrome("A man, a plan, a canal: Panama")) # expected output = True
    print(isPalindrome("race a car")) # expected output = False
    


