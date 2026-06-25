#QuickSelect approach
import random 
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDist(point: List[int]) -> int:
            return point[0]**2 + point[1]**2
        
        def partition(left, right, pivot_idx) -> int:
            pivot_dist = getDist(points[pivot_idx])
            points[pivot_idx], points[right] = points[right], points[pivot_idx]

            store_idx = left
            for i in range(left, right):
                if getDist(points[i]) < pivot_dist:
                    points[i], points[store_idx] = points[store_idx], points[i]
                    store_idx += 1
            
            points[right], points[store_idx] = points[store_idx], points[right]
            return store_idx

        left, right = 0, len(points) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)

            p = partition(left, right, pivot_idx)

            if p == k:
                break
            elif p > k:
                right = p - 1
            else:
                left = p + 1
        
        return points[0:k]

