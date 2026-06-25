#cache / memoization top-down approach
#O(n) time complexity

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2

            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n - 1) + climb(n - 2)
                return memo[n]

        return climb(n)