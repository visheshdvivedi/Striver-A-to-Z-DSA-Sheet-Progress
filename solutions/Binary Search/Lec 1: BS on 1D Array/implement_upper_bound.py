from typing import List

class Solution:
    def getFloorAndCeil(self, x: int, arr: List[int]) -> List[int]:
        start = 0
        end = len(arr) - 1
        floor = ceil = -1

        arr.sort()

        while start <= end:
            mid = start + ((end - start) // 2)
            if arr[mid] <= x:
                floor = arr[mid]
                start = mid + 1
            if arr[mid] >= x:
                ceil = arr[mid]
                end = mid - 1

        return [floor, ceil]