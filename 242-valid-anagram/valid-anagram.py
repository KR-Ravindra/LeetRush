class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # by sorting
        return sorted(s) == sorted(t)
 

        