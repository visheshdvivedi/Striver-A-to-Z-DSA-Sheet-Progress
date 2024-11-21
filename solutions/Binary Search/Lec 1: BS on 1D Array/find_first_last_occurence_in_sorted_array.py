from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1

        while (start <= end and nums[start] < target):
            start += 1

        while (start <= end and nums[end] > target):
            end -= 1

        if start > end:
            return [-1, -1]
        return [start, end]