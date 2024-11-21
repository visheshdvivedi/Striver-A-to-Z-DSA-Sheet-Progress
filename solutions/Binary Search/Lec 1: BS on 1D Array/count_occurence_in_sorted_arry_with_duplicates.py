class Solution:

    def binarySearch(self, arr, target, first=True):
        start = 0
        end = len(arr) - 1
        num = -1

        while start <= end:
            mid = start + ((end - start) // 2)
            if arr[mid] == target:
                num = mid
                if first:
                    end = mid - 1
                else:
                    start = mid + 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return num

    def countFreq(self, arr, target):
        first = self.binarySearch(arr, target)
        if first == -1: return 0
        last = self.binarySearch(arr, target, False)
        return last - first + 1