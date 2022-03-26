""" ------- Rotate Image -------
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
>>> DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 """


"""--------Approach 1: Rotate Groups of Four Cells---------"""
def rotateGroupCells(matrix):
    n = len(matrix[0])
    
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]  # bottom left of the matrix
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1] # bottom left replaced by bottom right
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i] # bottom right replaced by top right
            matrix[j][n - 1 - i] = matrix[i][j] # top right replaced by top left
            matrix[i][j] = tmp # top right replaced by tmp
    
    print(matrix)
    # Time: O(M) where M is the number of cells in the matrix 
    # Space: O(1)


# matrix = [[1,2,3],[4,5,6],[7,8,9]] 
# rotateGroupCells(matrix) # expected output = [[7,4,1],[8,5,2],[9,6,3]]

# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# rotateGroupCells(matrix) # expected output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


"""--------Approach 2: Reverse diagonal (Transpose) and reverse left to right---------"""
def rotate(matrix):
    transpose(matrix)
    reflect(matrix)
    print(matrix)


def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reflect(matrix): # reverse
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
    # Time: O(M) - M is the number of cells in the grid
    #            - Transposing and reversing has a cost of O(M) for each function for moving values of each cell
    # Space: O(1)

matrix = [[1,2,3],[4,5,6],[7,8,9]] 
rotate(matrix) # expected output = [[7,4,1],[8,5,2],[9,6,3]]

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix) # expected output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

