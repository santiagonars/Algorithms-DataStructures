""" ----------Add Binary----------
Problem:
>>> Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself. """

""" 
initize sum variable
initize carry variable 
get max length
while less than maxlen
    get digit1 and digit2
    multiple sum by 10
    if sum of digit1 and digit2 > 1: sum increases by 1 and carry increases by 1
    elif sum of digit1 and digit2 = 1: sum increases by 1
    eslse sum of digit1 and digit2 = 0: multiple sum by 10

sum => 1
"""
# >>> DRAWBACK: In Java, this approach is limited by the length of the input strings and if it's too long, the result will not fit
# Time Complexity => O(N + M)
# Space Complexity => O(1)
def addBinary(a, b):
    sum = int(a, 2) + int(b, 2)
    sum ='{0:b}'.format(sum)
    return sum


# Time Complexity => O(N + M) ,for the number of characters in each each string, a and b.
# Space Complexity => O(1)
def addBinary(a, b):
    sum = int(a, 2) + int(b, 2)
    sum ='{0:b}'.format(sum)
    return sum

# Time Complexity => O(max(N,M)) ,where N and M are the lengths of a and b respectively
# Space Complexity => O(max(N,M)) for the answer
def addBinary2(a, b):
    n = max(len(a), len(b))
    a = a.zfill(n) # .zfill(length) fills the string with zeros up to the length that is passed
    b = b.zfill(n) 

    carry = 0
    answer = []
    for i in range(n - 1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1
            
        if carry % 2 == 1:
            answer.append('1')
        else:
            answer.append('0')

        carry //= 2 # carry = carry // 2

    if carry == 1:
        answer.append('1')
    answer.reverse() # O(n) for reverse() function

    return ''.join(answer)


def main():
    a, b = "11", "1"
    print(addBinary(a, b)) # expect = "100"
    a, b = "1010", "1011"
    print(addBinary(a, b)) # expect = "10101"

    a, b = "11", "1"
    print(addBinary2(a, b)) # expect = "100"
    a, b = "1010", "1011"
    print(addBinary2(a, b)) # expect = "10101"

main()