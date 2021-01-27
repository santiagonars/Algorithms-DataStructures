""" ----------Set Matrix Zeoes----------
Problem:
>>> Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:
    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1 """

# ---- EXTRA SPACE NEEDED SOLUTION----
""" If any cell of the matrix has a zero we can record its row and column number. 
All the cells of this recorded row and column can be marked zero in the next iteration. """
# Time complexity: O(M * N) => M are the number of rows, and N are the number of columns
# Space complexity: O(M + N) to store row and column sets
def setZeroes(matrix):
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()
    # record rows and columnns that are to be zeroed
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # iterate again and zero out rows and columns with the sets 
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0
    
    print(matrix)


# ----MEMORY EFFICIENT (In-Place)----
""" Rather than using additional variables to keep track of rows and columns to be reset, we use the matrix itself as the indicators. 
>>> The idea is that we can use the first cell of every row and column as a flag."""
# Time complexity: O(M * N) => M are the number of rows, and N are the number of columns
# Space complexity: O(1)
def setZeroes_efficient(matrix):
    R = len(matrix)
    C = len(matrix[0])
    is_col = False
    
    for i in range(R):

        if matrix[i][0] == 0:
            is_col = True
        # If an element is zero, set the first element of the corresponding row and column to 0
        for j in range(1, C):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, R):
        for j in range(1, C):
            # if the first row or first column is 0 (Not False, hence True) of any element, set value to 0
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    # check if first row needs to be set to zero 
    if matrix[0][0] == 0:
        for j in range(C):
            matrix[0][j] = 0

    # check if first column needs to be set to zero
    if is_col:
        for i in range(R):
            matrix[i][0] = 0

    print(matrix)
    
    
def main():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes(matrix) # expected change = [[1,0,1],[0,0,0],[1,0,1]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    setZeroes(matrix) # expected change = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes_efficient(matrix) # expected change = [[1,0,1],[0,0,0],[1,0,1]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    setZeroes_efficient(matrix) # expected change = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


main()