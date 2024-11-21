from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_end = m - 1
        right_end = n - 1
        merge_end = m + n - 1

        while right_end >= 0:
            if left_end >= 0 and nums1[left_end] > nums2[right_end]:
                nums1[merge_end] = nums1[left_end]
                left_end -= 1
            else:
                nums1[merge_end] = nums2[right_end]
                right_end -= 1

            merge_end -= 1