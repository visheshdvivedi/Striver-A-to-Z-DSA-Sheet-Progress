class Solution:
    def fib(self, n: int) -> int:
        memo = { 0: 0, 1: 1 }

        def dp(n: int):
            if n in memo:
                return memo[n]
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]

        return dp(n)