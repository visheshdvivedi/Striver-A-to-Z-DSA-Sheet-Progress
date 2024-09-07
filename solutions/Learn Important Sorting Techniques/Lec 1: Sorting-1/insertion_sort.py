class Solution:
    def insert(self, alist, index, n):
        j = index - 1
        while j >= 0 and alist[j] > alist[j+1]:
            alist[j], alist[j+1] = alist[j+1], alist[j]
            j -= 1
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for i in range(1, n):
            self.insert(alist, i, n)