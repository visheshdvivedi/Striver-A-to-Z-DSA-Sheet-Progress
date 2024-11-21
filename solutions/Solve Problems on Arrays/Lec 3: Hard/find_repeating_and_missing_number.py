class Solution:
    def findTwoElement( self,arr):

        length = len(arr)
        expected = (length * (length + 1)) // 2
        actual = 0

        nums_dict = {}
        repeated = 0

        for num in arr:
            actual += num
            if num in nums_dict: repeated = num
            else: nums_dict[num] = 1

        missing = repeated + expected - actual
        return [repeated, missing]