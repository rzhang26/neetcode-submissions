from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1 * stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            y = heapq.heappop(max_heap) * -1
            x = heapq.heappop(max_heap) * -1

            if x < y:
                heapq.heappush(max_heap, (y - x) * -1)
        
        if not max_heap:
            return 0

        return max_heap[0] * -1