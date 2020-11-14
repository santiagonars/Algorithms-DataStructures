""" ----------Find missing number in range N to 1 Using XOR----------
Problem
>>> Given an array of (N - 1) integers in the range from 1 to N, find the one number that is missing from the array.

*** This solution prevents interger overflow when using XOR!
# NOTE: ^ is the XOR operation for python

Example:
Input: [1, 5, 2, 6, 4]
Answer: 3 """
# NOTE: Time complexity => O(N)
# NOTE: Space complexity => O(1)


def find_missing_number(arr):
    n = len(arr) + 1
    # x1 represents XOR of all values from 1 to n
    x1 = 1
    for i in range(2, n+1):
        print('{} ^ {}'.format(x1, i))
        x1 = x1 ^ i
        print("x1: ", x1)
    print()
    # x2 represents XOR of all values in arr
    x2 = arr[0]
    for i in range(1, n-1):
        print('{} ^ {}'.format(x2, i))
        x2 = x2 ^ arr[i]
        print("x2: ", x2)
    
    # missing number is the xor of x1 and x2
    return x1 ^ x2


# BAD: This solution can result in interger overflow if 'N' of the array is large enough
def find_missing_number_without_XOR(arr):
    n = len(arr) + 1
    # find sum of all numbers from 1 to n.
    s1 = 0
    for i in range (1, n+1):
        s1 += i

    # subtract all numbers in input from sum.
    for i in arr:
        s1 -= i
    
    # s1, now, is the missing number
    return s1


def main():
    arr = [1, 5, 2, 6, 4] 
    print('Missing number using XOR is: ' + str(find_missing_number(arr)))

    # print('Missing number NOT using XOR is: ' + str(find_missing_number_without_XOR(arr)))
		
main()
