from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if not grid:
            return -1
        if grid[0][0] == 1:
            return -1
        if grid[n-1][n-1] == 1:
            return -1

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        directions = [(-1, 1), (-1, 0), (-1, -1),
                        (0, 1), (0, -1),
                        (1, 1), (1, 0), (1, -1)]

        while queue:
            r, c, length = queue.popleft()

            if r == n - 1 and c == n - 1:
                return length
            
            for dr, dc in directions: #the values to help navigate curr node offsets (8-directional)
                next_r, next_c = r + dr, c + dc

                if 0 <= next_r < n and 0 <= next_c < n and grid[next_r][next_c] == 0:
                    queue.append((next_r, next_c, length + 1))
                    grid[next_r][next_c] = 1 #modify cell in-place to avoid infinite loop | alternative is using a set() for seen nodes
        
        return -1
        