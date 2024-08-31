class Solution:
    def factorialNumbers(self, n):
        multiplier = 1
        factorial = 1
        out = []
        while factorial <= n:
            out.append(factorial)
            multiplier += 1
            factorial *= multiplier
        return out