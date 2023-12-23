class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # by sorting
        # return sorted(s) == sorted(t)
        # by algorithm
        countS, countT = defaultdict(int), defaultdict(int)
        for index in range(len(s)):
            countS[s[index]] = 1 + countS.get(s[index], 0)
            countT[t[index]] = 1 + countT.get(t[index], 0)

        for key in countS:
            if countT[key] != countS[key]:
                return False
        return True

        