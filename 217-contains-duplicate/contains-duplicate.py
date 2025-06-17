class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # occurred = set()

        # for eachnum in nums:
        #     if eachnum in occurred:
        #         return True
        #     occurred.add(eachnum)
        # return False
        return len(nums) != len(set(nums))