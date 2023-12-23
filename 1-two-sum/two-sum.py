class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# Solution:
# -> for each number let us subtract it from target and see if the difference exists in list (but this `in` is a big problem O(n))
# -> let us maintain HashMap and keep storing the numbers we see into it, and check if the diff is in the hashmap instead of whole list which is O(1)
# -> This way we will immediately know the solution in O(n)
        seenHashMap = {}
        for index, num in enumerate(nums):
            if target-num in seenHashMap:
                return [index, seenHashMap[target-num]]
            seenHashMap[num] = index
        return False