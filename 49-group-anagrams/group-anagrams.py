class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for each in strs:
            count = [0] * 26
            for char in each:
                count[ord(char)-ord('a')] +=1
            key = tuple(count)
            if key in res:
                res[key].append(each)
            else:
                res[key] = [each]

        print(res)
        return res.values()