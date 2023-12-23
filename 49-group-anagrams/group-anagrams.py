class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_output = defaultdict(list)
        for str in strs:
            # count = [0] * 26

            # for char in str:
            #     count[ord(char)-ord('a')] += 1
            
            # final_output[tuple(count)].append(str)
            final_output[tuple(sorted(str))].append(str)
        
        return final_output.values()

            

