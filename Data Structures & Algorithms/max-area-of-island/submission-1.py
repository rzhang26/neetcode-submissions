class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0

        def DFS(r, c) -> int:

            if r < 0 or c < 0:
                return 0 
            if r >= len(grid) or c >= len(grid[0]):
                return 0
            
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return (1 + DFS(r + 1, c) 
            + DFS(r - 1, c)
            + DFS(r, c + 1)
            + DFS(r, c - 1))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    curr_area = DFS(row, col)
                    max_area = max(curr_area, max_area)

        return max_area