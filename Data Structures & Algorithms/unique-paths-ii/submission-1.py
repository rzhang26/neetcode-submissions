class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 1D array to represent the current row status
        dp = [0] * n
        
        # Base Case: Initialize the starting position if it's open
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c > 0:
                    # Current cell = Top cell (dp[c]) + Left cell (dp[c-1])
                    dp[c] += dp[c-1]
                    
        return dp[-1]