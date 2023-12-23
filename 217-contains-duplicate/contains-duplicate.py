class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
# solution:
# -> for each element we visit, let us store it in a hashset (why not list? 'in' operation in list is O(n); in set is O(1))
# -> for every element we see check in the hashset, if exists return True
#         seenHashSet = set()
#         for num in nums:
#             if num in seenHashSet:
#                 return True
#             seenHashSet.add(num)
#         return False
# by sorting:
# -> sort all the elements and then compare each other, none should be same
            sortednums = sorted(nums)
            print(sortednums)
            for i in range(len(sortednums)-1):
                if sortednums[i] == sortednums[i+1]:
                    return True
            return False
