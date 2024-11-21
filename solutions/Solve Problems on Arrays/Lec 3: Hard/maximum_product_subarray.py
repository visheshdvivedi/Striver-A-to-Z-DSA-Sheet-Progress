from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        output = curr_max

        for i in range(1, len(nums)):
            vals = (nums[i], nums[i] * curr_min, nums[i] * curr_max)
            curr_max = max(vals)
            curr_min = min(vals)
            output = max(curr_max, output)

        return output