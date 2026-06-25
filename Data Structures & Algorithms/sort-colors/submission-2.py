class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Pointers representing the boundaries where 0, 1, and 2 should end
        p0 = p1 = p2 = 0
        
        for num in nums:
            if num == 0:
                # A 0 expands all three zones forward
                nums[p2] = 2
                nums[p1] = 1
                nums[p0] = 0
                p0 += 1
                p1 += 1
                p2 += 1
            elif num == 1:
                # A 1 expands the 1 and 2 zones forward
                nums[p2] = 2
                nums[p1] = 1
                p1 += 1
                p2 += 1
            elif num == 2:
                # A 2 only expands the 2 zone forward
                nums[p2] = 2
                p2 += 1