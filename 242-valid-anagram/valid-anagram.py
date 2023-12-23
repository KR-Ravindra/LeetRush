class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
# solution:
# -> first check if both strings are same length if not then it is not anagaram
        if len(s) != len(t):
            return False
# by algorithm:
# -> count the frequency of characters into a hashmap and then compare both; if their hashmap is same then they are anagram
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # for each in countS:
        #     if countT.get(each, 0) != countS[each]:
        #         return False
        # return True
# by sorting:
# -> if both of their sorted inputs are same then they both are anagrams
        return sorted(s) == sorted(t)