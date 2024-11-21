from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if end == 0: return nums[0]

        while start <= end:
            mid = start + ((end - start) // 2)
            if mid > 0 and mid < len(nums) - 1:
                if nums[mid] == nums[mid-1]:
                    if mid % 2 == 0:
                        end = mid - 1
                    else:
                        start = mid + 1
                elif nums[mid] == nums[mid+1]:
                    if mid % 2 == 0:
                        start = mid + 1
                    else:
                        end = mid - 1
                else: return nums[mid]
            elif mid == 0:
                if nums[mid] == nums[mid + 1]: start = mid + 1
                else: return nums[mid]
            elif nums[mid] == nums[mid - 1]: start = mid + 1
            else: return nums[mid]