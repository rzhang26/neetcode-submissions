class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right  # Default to max possible rate
        
        while left <= right:
            mid = (left + right) // 2
            
            # Calculate total hours spent at rate 'mid'
            hours_spent = 0
            for pile in piles:
                # This performs ceiling division: math.ceil(pile / mid)
                hours_spent += (pile + mid - 1) // mid
                
            # Check if Koko can finish within h hours
            if hours_spent <= h:
                res = mid          # Track this as a possible answer
                right = mid - 1    # Try to find a smaller/slower valid rate
            else:
                left = mid + 1     # Too slow! We need a faster rate
                
        return res