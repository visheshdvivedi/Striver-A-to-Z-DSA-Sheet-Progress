from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = False
        row0 = False

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:

                    # for first row and column
                    if row == 0:
                        row0 = True
                    elif col == 0:
                        col0 = True

                    # for other rows and columsn
                    else:
                        matrix[row][0] = 0
                        matrix[0][col] = 0

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == 0 and row0:
                    matrix[row][col] = 0
                elif col == 0 and col0:
                    matrix[row][col] = 0
                elif matrix[row][0] == 0:
                    matrix[row][col] = 0
                elif matrix[0][col] == 0:
                    matrix[row][col] = 0