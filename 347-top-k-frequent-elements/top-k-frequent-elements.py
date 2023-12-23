class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        frequency = [set() for i in range(len(nums)+1)]
        for each in count:
            frequency[count[each]].add(each)
        result = []
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result

            