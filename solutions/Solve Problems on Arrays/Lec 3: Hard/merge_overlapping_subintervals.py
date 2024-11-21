from typing import List

class Solution:
    def is_overlapping(self, first: List[int], second: List[int]) -> bool:
        if second[0] >= first[0] and second[0] <= first[1]:
            return True
        elif second[1] >= first[0] and second[1] <= first[1]:
            return True
        return False

    def merge_intervals(self, first: List[int], second: List[int]) -> List[int]:
        return [min(first[0], second[0]), max(first[1], second[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []

        intervals.sort()
        curr = intervals[0]

        for i in range(1, len(intervals)):
            if self.is_overlapping(curr, intervals[i]):
                curr = self.merge_intervals(curr, intervals[i])
            else:
                output.append(curr)
                curr = intervals[i]

        output.append(curr)
        return output