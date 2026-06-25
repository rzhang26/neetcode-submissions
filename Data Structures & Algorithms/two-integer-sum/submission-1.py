class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        def solve(i: int, seen: dict) -> list[int]:
            complement = target - nums[i]
            
            # If we've seen the complement before, we are done!
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, remember the current number and its index
            seen[nums[i]] = i
            
            # Move to the next index recursively
            return solve(i + 1, seen)
            
        return solve(0, {})