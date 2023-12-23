class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# solution:
# -> First we will calculate the count of each character/number
# -> then we plot it on frequency array, here frequency array could only be as big as len(nums)
# -> we reverse iterate through our frequency array ([6: {1,2}, 5: {2,3}....]) and fill result list with the variable we have in set till k is len(result)
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

            