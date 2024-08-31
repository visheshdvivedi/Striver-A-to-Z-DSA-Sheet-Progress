import math

class Solution:
    def switchCase(self, choice, arr):
        if choice == 1:
            return math.pow(arr[0], 2) * math.pi
        elif choice == 2:
            return arr[0] * arr[1]