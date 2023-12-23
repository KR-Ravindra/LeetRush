class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# Solution:
# -> algorithm way: 
# -> every string can only have characters from a-z (ascii 63-89 whatever); so for each str we will calculate the array[ascii 26]; this way if two strings are anagram their array[ascii 26] would be same. 
# -> then for each key we will have a list of str as values in our new hashmap
# -> return the values as list
        # resultHashMap = defaultdict(list)
        # for str in strs:
        #     count = [0]*26
        #     for char in str:
        #         count[ord(char)-ord('a')] += 1
        #     resultHashMap[(tuple(count))].append(str)
        # return resultHashMap.values()

# -> sorting way:
# -> if a string is anagram of other then their resultant sort should be same; for each str we will sort them
# -> sorted str is key and value is list of str that match this sorted pattern ( aet: [eat, tea])
# -> we return the values in list format for desired output
        resultHashMap = defaultdict(list)
        for str in strs:
            resultHashMap[tuple(sorted(str))].append(str)
        return resultHashMap.values()
            

