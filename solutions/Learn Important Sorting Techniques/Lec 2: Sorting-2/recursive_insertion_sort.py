class Solution:
    def insert(self, alist, n, i, j):
        if j < 0: return
        elif alist[j] > alist[j+1]:
            alist[j], alist[j+1] = alist[j+1], alist[j]
        self.insert(alist, n, i, j-1)
           
    def insertionSort(self, alist, n):
        for i in range(1, n):
            self.insert(alist, n, i, i-1)