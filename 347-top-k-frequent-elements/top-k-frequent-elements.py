class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# solution:
# -> First we will calculate the count of each character/number
# -> then we plot it on frequency array, here frequency array could only be as big as len(nums)
# -> we reverse iterate through our frequency array ([6: {1,2}, 5: {2,3}....]) and fill result list with the variable we have in set till k is len(result)
        countHashMap = defaultdict(int)

        for num in nums:
            countHashMap[num] += 1
        
        frequency_array = [[] for i in range(len(nums)+1)]
        print(frequency_array)
        for keys, values in countHashMap.items():
            frequency_array[values].append(keys)
        
        result = []
        for eachList in frequency_array[::-1]:
            for each in eachList:
                result.append(each)
                if len(result) == k:
                    return result