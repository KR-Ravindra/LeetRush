class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existing = set(nums)
        if len(existing) == len(nums):
            return False
        return True
        