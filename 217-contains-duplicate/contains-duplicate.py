class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # by using hashset
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        # by using list
        # seen = []
        # for num in nums:
        #     if num in seen:
        #         return True
        #     else:
        #         seen.append(num)
        # return False