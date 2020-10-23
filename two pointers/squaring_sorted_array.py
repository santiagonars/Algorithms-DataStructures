""" ----------Squaring a Sorted Array (easy)----------
Problem Statement:
>>> Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9] """
# NOTE: Time complexity => O(N) => linear bc we only need to loop through array items; could be O(N + 1/2N) which is asymptotically equivalent
# NOTE: Space complexity => O(N) => equivalent to output array

def make_squares(arr):
    n = len(arr)
    squares = [0 for i in range(n)] # create array to put the squared results
    left, right = 0, n - 1
    highestIndex = n - 1
    while left <= right:
        squared_left = arr[left] * arr[left]
        squared_right = arr[right] * arr[right]
        # if squared_left is greater, we add it to the highest index in resultant array and increase left index by 1 position down the input array
        if squared_left > squared_right:
            squares[highestIndex] = squared_left
            left += 1
        # if squared_right is equal of greater, we add it to the highest index in the resultant array and decrease right index by 1 position
        else: 
            squares[highestIndex] = squared_right
            right -= 1
        highestIndex -= 1

    return squares


if __name__ == "__main__":
    array_test = [-2, -1, 0, 2, 3]
    print(make_squares(array_test)) # expected output = [0, 1, 4, 4, 9]
    array_test = [-3, -1, 0, 1, 2]
    print(make_squares(array_test)) # expected output = [0, 1, 1, 4, 9]