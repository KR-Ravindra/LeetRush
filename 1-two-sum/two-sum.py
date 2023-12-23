class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, eachnum in enumerate(nums):
            diff = target-eachnum
            if diff in seen:
                return [index, seen[diff]]
            seen[eachnum] = index