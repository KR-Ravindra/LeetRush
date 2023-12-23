class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        frequency = [[] for i in range(len(nums)+1)]
        for eachnum in nums:
            map[eachnum] = 1 + map.get(eachnum, 0)
        for key, value in map.items():
            frequency[value].append(key)
        res = []
        for i in range(len(frequency)-1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res