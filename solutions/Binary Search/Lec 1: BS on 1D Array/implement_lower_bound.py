class Solution:
    def findFloor(self,arr,k):
        start = 0
        end = len(arr) - 1
        answer = -1

        while start <= end:
            mid = start + ((end - start) // 2)
            if arr[mid] <= k:
                answer = mid
                start = mid + 1
            else: end = mid - 1

        return answer