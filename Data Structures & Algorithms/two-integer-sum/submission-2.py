class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        def solve(i: int) -> list[int]:
            # Scan through the rest of the array looking for the partner
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            
            # If not found, look for a pair starting from the next index
            return solve(i + 1)
            
        return solve(0)