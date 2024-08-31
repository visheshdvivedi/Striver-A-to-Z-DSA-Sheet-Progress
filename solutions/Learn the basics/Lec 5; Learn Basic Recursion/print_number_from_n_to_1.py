class Solution:
    def recursiveCall(self, n):
        if n <= 0:
            return
        print(n, end=" ")
        self.recursiveCall(n-1)
    def printNos(self, n):
        self.recursiveCall(n)