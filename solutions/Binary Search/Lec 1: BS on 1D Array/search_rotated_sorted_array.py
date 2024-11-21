from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + ((end - start) // 2)

            if nums[mid] == target: return mid
            elif nums[start] == target: return start
            elif nums[end] == target: return end

            # check if left array is sorted
            elif nums[start] < nums[mid]:

                # check if target is between these two
                if target < nums[mid] and target > nums[start]:
                    end = mid - 1

                # target is in right side
                else:
                    start = mid + 1

            # check if right array is sorted
            else:

                # check if target is between these two
                if target < nums[end] and target > nums[mid]:
                    start = mid + 1

                # target is in left side
                else:
                    end = mid - 1

        return -1