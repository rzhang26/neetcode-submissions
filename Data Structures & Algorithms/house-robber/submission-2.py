#memoization / cache approach

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def calcMax(i):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            rob_curr = nums[i] + calcMax(i - 2)
            skip_curr = calcMax(i - 1)

            memo[i] = max(rob_curr, skip_curr)
            return memo[i]
            

        #start from back of house list
        return calcMax(len(nums) - 1)