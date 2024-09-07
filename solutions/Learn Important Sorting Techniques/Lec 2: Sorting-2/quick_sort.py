class Solution:
    
    def quickSort(self,arr,low,high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot-1)
            self.quickSort(arr, pivot+1, high)
        
    def partition(self,arr,low,high):
        pivot = arr[low]
        
        leftptr = low
        rightptr = high
        
        while (leftptr < rightptr):
            while (arr[leftptr] <= pivot and leftptr < high):
                leftptr += 1
            while (arr[rightptr] > pivot and rightptr > low):
                rightptr -= 1
            if leftptr < rightptr:
                arr[leftptr], arr[rightptr] = arr[rightptr], arr[leftptr]
                    
        
        arr[low], arr[rightptr] = arr[rightptr], arr[low]
        return rightptr
