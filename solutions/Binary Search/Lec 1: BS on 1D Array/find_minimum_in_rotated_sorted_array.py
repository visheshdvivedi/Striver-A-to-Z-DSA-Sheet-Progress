class Solution:

    def findMin(self, nums) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + ((end - start) // 2)

            # both left and right sides are sorted
            if nums[start] <= nums[mid-1] and nums[mid] <= nums[end]:
                if nums[start] < nums[mid]: return start
                else: return mid

            # only left array is sorted
            elif nums[start] <= nums[mid]: start = mid + 1

            # only right array is sorted
            else: end = mid - 1

        return end

    def findKRotation(self, arr):

        # find min element index
        minValIndex = self.findMin(arr)

        # return how left the element is
        return minValIndex - 0