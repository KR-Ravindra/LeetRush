class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s = {}
        frequency_t = {}
        if len(s) == len(t):
            for each in s:
                if each in frequency_s.keys():
                    frequency_s[each] += 1
                else:
                    frequency_s[each] = 1
            for each in t:
                if each in frequency_t.keys():
                    frequency_t[each] += 1
                else:
                    frequency_t[each] = 1
            if frequency_s == frequency_t:
                return True
        else:
            return False
        return False

        