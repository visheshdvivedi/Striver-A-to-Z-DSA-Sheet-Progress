class Solution:
    def merge(self, arr, left, mid, right):
        arr1 = arr[left:mid+1]
        arr2 = arr[mid+1:right+1]
        final = [0] * (right - left + 1)

        len1 = len(arr1)
        len2 = len(arr2)

        leftptr = 0
        rightptr = 0
        finalptr = 0

        while leftptr < len1 and rightptr < len2:
            if arr1[leftptr] < arr2[rightptr]:
                final[finalptr] = arr1[leftptr]
                leftptr += 1
            else:
                final[finalptr] = arr2[rightptr]
                rightptr += 1
            finalptr += 1

        while leftptr < len1:
            final[finalptr] = arr1[leftptr]
            finalptr += 1
            leftptr += 1

        while rightptr < len2:
            final[finalptr] = arr2[rightptr]
            finalptr += 1
            rightptr += 1

        for i in range(finalptr):
            arr[left+i] = final[i]

    def mergeSort(self, arr, left, right):
        if left == right:
            return
        
        mid = left + ((right - left) // 2)
        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid+1, right)
        self.merge(arr, left, mid, right)