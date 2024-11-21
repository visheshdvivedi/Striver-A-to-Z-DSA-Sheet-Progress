import math
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix: return []

        rows = len(matrix)
        cols = len(matrix[0])
        output = []
        depth_end = math.ceil(min(rows, cols)/2)

        for depth in range(depth_end):

            # iterate top row
            for col in range(depth, cols - depth):
                output.append(matrix[depth][col])

            # iterate right column
            for row in range(depth + 1, rows - depth):
                output.append(matrix[row][cols-depth-1])

            if rows - depth - 1 > depth:
                for col in range(cols-depth-2, depth-1, -1):
                    output.append(matrix[rows-depth-1][col])

            # iterate left column
            if cols - depth - 1 > depth:
                for row in range(rows-depth-2, depth, -1):
                    output.append(matrix[row][depth])

        return output