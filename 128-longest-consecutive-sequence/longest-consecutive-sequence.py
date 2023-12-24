class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        numSet = set(nums)
        for eachnum in numSet:
            if eachnum - 1 not in numSet:
                length = 0
                while eachnum+length in numSet:
                    length += 1
                longest_length = max(length, longest_length)
        return longest_length
