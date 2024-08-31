class Solution:    
    def recursiveCall(self, curr, n):
        if curr > n:
            return
        print(curr, end=" ")
        self.recursiveCall(curr+1, n)
    
    def printNos(self,N):
        self.recursiveCall(1, N)