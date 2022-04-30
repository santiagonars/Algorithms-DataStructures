""" ------- Maximal Rectangle -------
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
    rows == matrix.length
    cols == matrix[i].length
    1 <= row, cols <= 200
    matrix[i][j] is '0' or '1'. """


""" ----- SOLUTION: Dynamic Programming - Better Brute Force on Histograms ----- 
>>> First find maxWidth for a rectangle that ends at every coordinate using:
        row[i] = row[i - 1] + 1 if row[i] == '1'
>>> Find global max rectangle by iterating up a column for every cordinate:
        maxWidth = min(maxWidth, currenWidth)
        currentArea = maxWidth * (currenRow - initialRow + 1)
        maxArea = max(maxArea, currentArea)
*** Precomputing the max width breaks into turned histogram, and we are finding the area of each one. 
> This approach improves on the brute force solution """

def maximalRectangle(matrix):
    max_area = 0
    
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if matrix[i][j] == "0": continue

            # compute max width and store it
            width = dp[i][j] = dp[i][j-1] + 1 if matrix[i][j] == "1" else 0
            # width = dp[i][j] = dp[i][j-1] + 1 if j else 1

            # compute max rectangle using lower right corner @ [i, j]
            for k in range(i, -1, -1):
                width = min(width, dp[k][j])
                max_area = max(max_area, width * (i-k+1))

    return max_area
    # O(N^2*M) time: iterate over the values in the same column + doing it for all N * M points
    # O(N*M) space to store max witth of every coordinate 
    #        where N is number of rows and M is number of columns


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalRectangle(matrix)) # expect: 6

matrix = [["0"]]
print(maximalRectangle(matrix)) # expect: 0

matrix = [["1"]]
print(maximalRectangle(matrix)) # expect: 1



""" ----- SOLUTION: Using Histograms - Stack ----- """