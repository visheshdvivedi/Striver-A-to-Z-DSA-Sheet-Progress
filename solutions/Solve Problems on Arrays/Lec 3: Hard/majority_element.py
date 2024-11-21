from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        total = len(nums)
        counter = Counter(nums)

        limit = len(nums) / 3
        output = []
        for num in counter:
            if counter[num] > limit:
                output.append(num)

        return output