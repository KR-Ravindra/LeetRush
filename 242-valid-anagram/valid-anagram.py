class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
# solution:
# -> first check if both strings are same length if not then it is not anagaram
        if len(s) != len(t):
            return False
# by algorithm:
# -> count the frequency of characters into a hashmap and then compare both; if their hashmap is same then they are anagram
        countS, countT = defaultdict(int), defaultdict(int)
        for each in s:
            countS[each] += 1
        for each in t:
            countT[each] += 1
        for keys, values in countS.items():
            if values == countT[keys]:
                continue;
            else:
                return False
        return True
            
# by sorting:
# -> if both of their sorted inputs are same then they both are anagrams
        # return sorted(s) == sorted(t)