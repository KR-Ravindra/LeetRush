class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        result = []
        frequency = [set() for i in range(len(nums)+1)]
        for eachnum in nums:
            count[eachnum] += 1

        for eachnum in nums:
            frequency[count[eachnum]].add(eachnum)
        
        print(count, frequency)
        for i in range(len(frequency)-1, 0, -1):
            for eachnum in frequency[i]:
                result.append(eachnum)
                if len(result) == k:
                    return result
        