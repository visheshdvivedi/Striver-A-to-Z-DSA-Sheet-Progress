class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if n == m: return "equal"
        elif n < m: return "lesser"
        return "greater"