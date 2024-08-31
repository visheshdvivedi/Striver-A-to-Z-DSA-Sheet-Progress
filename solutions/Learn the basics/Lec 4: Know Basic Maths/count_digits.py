class Solution:
    def evenlyDivides (self, N):
        count = 0
        temp = N
        while temp > 0:
            digit = temp % 10
            if digit != 0 and N % digit == 0: count += 1
            temp = temp // 10
        return count
