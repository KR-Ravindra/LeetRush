class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# solution:
# -> First we will calculate the count of each character/number
# -> then we plot it on frequency array, here frequency array could only be as big as len(nums)
# -> we reverse iterate through our frequency array ([6: {1,2}, 5: {2,3}....]) and fill result list with the variable we have in set till k is len(result)
        countHashMap = defaultdict(int)
        for each in nums:
            countHashMap[each] += 1
        
        frequency = [[] for i in range(len(nums)+1)]
        for number, count in countHashMap.items():
            frequency[count].append(number)
        
        result = []
        for each in frequency[::-1]:
            for eachElement in each:
                result.append(eachElement)
            if len(result) == k:
                return result
        
        return False