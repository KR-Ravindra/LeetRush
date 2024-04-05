class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
# solution:
# -> for each element we visit, let us store it in a hashset (why not list? 'in' operation in list is O(n); in set is O(1))
# -> for every element we see check in the hashset, if exists return True
        # seen = set()
        # for each in nums:
        #     if each in seen:
        #         return True
        #     else:
        #         seen.add(each)
        # return False
# by sorting:
# -> sort all the elements and then compare each other, if any same then we have duplicate
        # nums.sort()
        # for index, num in enumerate(nums):
        #     if index+1 <=len(nums)-1:
        #         if nums[index+1] == num:
        #             return True
        # return False
# by comparing lenght of array and its set:
            return not len(nums) == len(set(nums))