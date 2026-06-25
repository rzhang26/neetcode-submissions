# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            
            if res == 0:
                # Found the picked number
                return mid
            elif res == -1:
                # Guess is too high, look lower
                right = mid - 1
            else:
                # Guess is too low, look higher
                left = mid + 1
                
        return -1