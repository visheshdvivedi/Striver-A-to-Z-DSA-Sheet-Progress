class Solution: 
    def select(self, arr, n, i):
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        return minIndex
    
    def selectionSort(self, arr,n):
        for i in range(n-1):
            minIndex = self.select(arr, n, i)
            if minIndex != i:
                arr[minIndex], arr[i] = arr[i], arr[minIndex]