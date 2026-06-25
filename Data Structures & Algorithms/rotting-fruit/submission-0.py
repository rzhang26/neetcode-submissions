from collections import deque

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        while queue and fresh_count > 0:
            minutes += 1

            qlen = len(queue)
            for _ in range(qlen):
                r, c = queue.popleft()

                for dr, dc in directions:
                    next_r, next_c = r + dr, c + dc

                    if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == 1:
                        grid[next_r][next_c] = 2
                        fresh_count -= 1
                        queue.append((next_r, next_c))

        return minutes if fresh_count == 0 else -1
