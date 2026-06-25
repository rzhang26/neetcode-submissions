class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        island_count = 0

        def DFS(r: int , c: int):
            if r < 0 or c < 0:
                return
            if r >= len(grid) or c >= len(grid[0]):
                return

            if grid[r][c] == '0':
                return 

            grid[r][c] = '0'

            DFS(r + 1, c)
            DFS(r - 1, c)
            DFS(r, c + 1)
            DFS(r, c - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    island_count += 1
                    DFS(row, col)
        
        return island_count
        
