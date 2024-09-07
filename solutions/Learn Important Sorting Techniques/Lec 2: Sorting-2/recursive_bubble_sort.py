class Solution:
    def bubbleSort(self,arr, n):
        if n>1:
            for j in range(n-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
            self.bubbleSort(arr,n-1)