from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0: return []
        elif numRows == 1: return [[1]]
        elif numRows == 2: return [[1], [1, 1]]

        output = [[1], [1, 1]]
        last_row = output[-1]
        for i in range(numRows+1):
            if i <= 2: continue
            arr = []
            for j in range(i):
                if j == 0 or j == i - 1: arr.append(1)
                else: arr.append(last_row[j-1] + last_row[j])
            output.append(arr)
            last_row = arr

        return output