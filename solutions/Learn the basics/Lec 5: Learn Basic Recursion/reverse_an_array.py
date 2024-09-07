class Solution:
    def reverseArray(self, arr):
        length = len(arr)
        left = 0
        right = length - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1