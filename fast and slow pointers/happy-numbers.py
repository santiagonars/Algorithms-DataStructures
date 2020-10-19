""" ----------Happy Number (medium)----------
Problem Statement #
>>> Any number will be called a happy number if, after repeatedly replacing it with a number equal to 
the sum of the square of all of its digits, leads us to number ‘1’. 
All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

NOTE: To find if a number is a happy number or not, always ends in a cycle! 

>>> Example 1:
Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:

1.)     2^2 + 3^2 = 4 + 9 = 13


2.)     1^2 + 3^2 = 1 + 9 = 10


3.)     1^2 + 0^2​ = 1 + 0 = 1 

>>> Example 2:
Input: 12   
Output: false (12 is not a happy number)  
Explanations: After 13 steps, Step ‘13’ leads us back to step ‘5’ as the number becomes equal to ‘89’, 
              this means that we can never reach ‘1’, therefore, ‘12’ is not a happy number. """
# NOTE: Time complexity => O(logN) => all unhappy numbers eventually get stuck in the cycle,
#                                  => TODO: need to look up why more to understand it better
# NOTE: Space complexity => O(1)


def find_happy_number(num):
    slow, fast = num, num
    # if  cycle converges to '1', that's where the 2 pointers will meet
    while True:
        slow = find_square_sum(slow) # move by one step
        fast = find_square_sum(find_square_sum(fast)) # move by two steps
        if slow == fast:
            break
    return slow == 1 # will be True if the cycle gets stuck at '1'


def find_square_sum(num):
    _sum = 0
    while (num > 0):
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()