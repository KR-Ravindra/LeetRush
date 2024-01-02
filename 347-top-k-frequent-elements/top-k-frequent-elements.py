class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# solution:
# -> First we will calculate the count of each character/number
# -> then we plot it on frequency array, here frequency array could only be as big as len(nums)
# -> we reverse iterate through our frequency array ([6: {1,2}, 5: {2,3}....]) and fill result list with the variable we have in set till k is len(result)
        countHashMap = defaultdict(int)

        for eachnum in nums:
            countHashMap[eachnum] += 1
        
        frequencyList = [[] for i in range(len(nums))]
        print(frequencyList)
        for num, value in countHashMap.items():
            frequencyList[value-1].append(num)
        
        result = []
        for each in frequencyList[::-1]:
            for eachnum in each:
                result.append(eachnum)
                if len(result) == k:
                    return result