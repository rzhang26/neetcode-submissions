import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points: # interesting for loop characteristic
            dist_squared = (x ** 2) + (y ** 2)

            heapq.heappush(max_heap, [-1 * dist_squared, [x, y]])

            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        return [point for dist, point in max_heap]