import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            # Calculate squared distance to avoid floating point issues
            dist = (x ** 2) + (y ** 2)
            
            # Python's heapq is a min-heap, so we push negative distances 
            # to mimic a max-heap behavior.
            heapq.heappush(max_heap, (-dist, [x, y]))
            
            # If the heap size exceeds k, get rid of the point that is farthest away
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # Extract the coordinate points from the heap
        return [point for dist, point in max_heap]