class Solution:
    def reverse(self, x: int) -> int:
        negative = bool(x < 0)
        left, right = pow(-2, 31), pow(2, 31) - 1
        reverse = int(str(abs(x))[::-1])
        
        if reverse < left or reverse > right: return 0
        elif negative: return -reverse
        return reverse