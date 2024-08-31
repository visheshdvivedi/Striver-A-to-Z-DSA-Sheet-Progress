class Solution:
    def recursiveCall(self, n):
        if n == 0:
            return
        print("GFG", end=" ")
        self.recursiveCall(n-1)
    def printGfg(self, n):
        self.recursiveCall(n)