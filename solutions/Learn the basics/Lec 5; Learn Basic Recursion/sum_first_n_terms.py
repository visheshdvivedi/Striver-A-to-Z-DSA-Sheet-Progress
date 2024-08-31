class Solution:
    def sumOfSeries(self,n):
        if n == 1:
            return 1
        return (n ** 3) + self.sumOfSeries(n - 1)