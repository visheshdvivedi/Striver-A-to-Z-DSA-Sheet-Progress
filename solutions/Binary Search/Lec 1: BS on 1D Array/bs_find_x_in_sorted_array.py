from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = length - 1

        if length == 1:
            if nums[0] == target: return 0
            else: return -1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid + 1
            else: right = mid - 1

        return -1