import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums) - k
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pivot_idx = random.randint(left, right)
            pivot_val = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            store_idx = left
            for i in range(left, right):
                if nums[i] <= pivot_val:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1
                
            nums[store_idx], nums[right] = nums[right], nums[store_idx]

            if store_idx == target_idx:
                return nums[store_idx]
            elif store_idx < target_idx:
                left = store_idx + 1
            else:
                right = store_idx - 1
        
        return -1

