class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i: int, curr_subset: List[int], curr_target: int):
            if curr_target == 0:
                res.append(curr_subset.copy())
                return
            if curr_target < 0:
                return 
            if i == len(nums):
                return 
            
            curr_subset.append(nums[i])
            backtrack(i, curr_subset, curr_target - nums[i])

            curr_subset.pop()
            backtrack(i + 1, curr_subset, curr_target)
        
        backtrack(0, [], target)
        return res