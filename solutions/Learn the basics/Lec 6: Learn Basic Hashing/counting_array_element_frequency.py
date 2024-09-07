class Solution:
    
    def frequencyCount(self, arr, N, P):
        hashlist = [0] * P
        for i in range(N):
            hashlist[arr[i]-1] += 1
            
        for i in range(min(N, P)):
            arr[i] = hashlist[i]
            
        if N > P:
            for i in range(P, N):
                arr[i] = 0