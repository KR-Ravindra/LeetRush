class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
# solution:
# - by algorithm:
# -> image a number line of these each elements, for consecuitive there is no left neighbour.
# -> if there is no left neighbour, we have to initiate length counting and then count till the next number exists in loop.
# -> finally see if longest<length and update; at end of loop return 
        longest = 0
        numSet  = set(nums)
        for num in numSet:
            if num-1 not in numSet:
                length = 1
                while num+length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

# solution:
# - by sorting:
# sort numbers and then see if difference is 1 (means consecutive..); then keep counting till length increases..
# here we convert sortednums to set because; `in` operation for set is O(1)
# solution comes of O(nlogn) and time exceeds
        nums.sort()
        longest = 0
        for index, num in enumerate(nums):
            length = 1
            while num+length in nums:
                length += 1
            longest = max(length, longest)
        return longest
