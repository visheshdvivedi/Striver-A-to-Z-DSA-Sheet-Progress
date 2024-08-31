class Solution:
    def sumOfDivisors(self, n):
        output = 0
        for i in range(1, n+1):
            output += i * (n // i)
        return output