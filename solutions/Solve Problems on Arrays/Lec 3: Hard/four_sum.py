from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []

        nums.sort()
        output = []
        i = j = 0

        while i < len(nums):
            if i == 0 or nums[i] != nums[i-1]:
                # perform acion
                j = i + 1
                while j < len(nums):
                    if j == i + 1 or nums[j] != nums[j-1]:
                        # perform action
                        start = j + 1
                        end = len(nums) - 1
                        while start < end:
                            total = nums[i] + nums[j] + nums[start] + nums[end]

                            if total == target:
                                output.append([nums[i], nums[j], nums[start], nums[end]])

                                start += 1
                                while (start < end and nums[start] == nums[start - 1]):
                                    start += 1

                                end -= 1
                                while (start < end and nums[end] == nums[end + 1]):
                                    end -= 1

                            elif total < target:
                                start += 1
                                while (start < end and nums[start] == nums[start - 1]):
                                    start += 1

                            else:
                                end -= 1
                                while (start < end and nums[end] == nums[end + 1]):
                                    end -= 1

                    j += 1
            i += 1

        return output