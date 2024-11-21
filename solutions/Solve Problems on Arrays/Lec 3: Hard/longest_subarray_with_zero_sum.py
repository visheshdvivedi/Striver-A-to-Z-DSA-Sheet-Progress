class Solution:
    def maxLen(self, arr):
        prefixSum = []
        currSum = 0

        for num in arr:
            currSum += num
            prefixSum.append(currSum)

        largest = 0
        indexes = {}
        for index, num in enumerate(prefixSum):
            if num == 0:
                largest = max(largest, index + 1)
            elif num in indexes:
                length = index - indexes[num]
                largest = max(largest, length)
            else:
                indexes[num] = index

        return largest
