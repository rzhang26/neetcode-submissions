class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        #DFS approach
        def backtrack(index: int, curr_subset: List[int]):
            if index == len(nums):
                res.append(curr_subset.copy())
                return 
            
            curr_subset.append(nums[index]) # *include* new num | left sub-tree so to speak
            backtrack(index + 1, curr_subset)

            curr_subset.pop() # *exclude* new num | right sub-tree so to speak
            backtrack(index + 1, curr_subset)

        backtrack(0, [])

        return res

