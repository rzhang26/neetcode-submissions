class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        island_max = 0
        island_area = 0

        def DFS(r, c):
            nonlocal island_area

            if r < 0 or c < 0:
                return
            if r >= len(grid) or c >= len(grid[0]):
                return 
            
            if grid[r][c] == 0:
                return 

            grid[r][c] = 0
            island_area += 1

            DFS(r + 1, c)
            DFS(r - 1, c)
            DFS(r, c + 1)
            DFS(r, c - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    island_area = 0
                    DFS(row, col)
                    island_max = max(island_area, island_max)

        return island_max
