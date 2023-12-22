class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS, mapT = {}, {}
        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        for key in mapS:
            if mapS[key] == mapT.get(key, 0):
                continue
            else:
                return False
        return True
 

        