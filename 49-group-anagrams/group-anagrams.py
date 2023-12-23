class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for each in strs:
            #using count O(size of list * n (size of each character))
            # count = [0] * 26
            # for char in each:
            #     count[ord(char)-ord('a')] +=1
            # key = tuple(count)
            # if key in res:
            #     res[key].append(each)
            # else:
            #     res[key] = [each]
            #using sorted array O(mnlogn)
            res[''.join(sorted(each))].append(each)

        print(res)
        return res.values()