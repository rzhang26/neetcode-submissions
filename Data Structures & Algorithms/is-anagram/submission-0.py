class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)


        # char_seen = set()

        # for char in s:
        #     char_seen.add(char)

        # for char in t:
        #     if char in char_seen:
        #         char_seen.remove(char)
        #     else:
        #         return False
        
        # return True