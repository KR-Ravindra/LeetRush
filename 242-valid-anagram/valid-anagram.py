class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        first = {}
        second = {}

        for eachS in s:
            first[eachS] = first.get(eachS, 0 ) + 1
        for eachT in t:
            second[eachT] = second.get(eachT, 0) + 1
        
        return first == second
            
