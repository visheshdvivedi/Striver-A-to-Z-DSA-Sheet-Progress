from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        output = set()
        for i in range(len(nums)):
            diff_dict = {}

            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                required = - nums[j] - nums[i]
                if required in diff_dict.keys():
                    output.add( tuple(sorted([nums[i], nums[j], required])) )
                diff_dict[nums[j]] = j

        return list(output)