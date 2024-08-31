class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        temp = abs(x)
        while temp > 0:
            digit = temp % 10
            output = (output * 10) + digit
            temp //= 10
        
        if output > pow(2, 31): return 0
        elif x < 0: return -output
        return output