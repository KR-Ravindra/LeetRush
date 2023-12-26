class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# solution:
# -> First we will calculate the count of each character/number
# -> then we plot it on frequency array, here frequency array could only be as big as len(nums)
# -> we reverse iterate through our frequency array ([6: {1,2}, 5: {2,3}....]) and fill result list with the variable we have in set till k is len(result)
        count = defaultdict(int)
        result = []
        for num in nums:
            count[num] += 1
        frequency = [[] for i in range(len(nums)+1)]
        for each, values in count.items():
            frequency[values].append(each)
        for each in frequency[::-1]:
            for eachlistitem in each:
                result.append(eachlistitem)
                if len(result) == k:
                    return result
        return False