class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        tot = 0
        for num in nums: 
            if(num == 1):
                tot += 1
                if(tot > max_one):
                    max_one = tot
            else:
                tot = 0
        return max_one
