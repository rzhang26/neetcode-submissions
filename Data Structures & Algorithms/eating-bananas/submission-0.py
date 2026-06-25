from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcHours(piles: List[int], rate: int) -> int:
            totHour = 0
            for pile in piles:
                totHour += (pile + rate - 1) // rate #ceiling division
            return totHour

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            hour_spent = calcHours(piles, mid)

            if hour_spent <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res