class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}

        def helper(self, stair: int) -> int:
        
            if stair == 1:
                return 1
            if stair == 2:
                return 2

            if stair in self.memo:
                return self.memo[stair]
            else:
                self.memo[stair] = helper(self, stair - 1) + helper(self, stair - 2)
            return self.memo[stair]

        return helper(self, n)