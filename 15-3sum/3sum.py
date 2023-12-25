class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for index, num in enumerate(nums):
            if index>0 and nums[index-1] == num:
                continue
            
            left, right = index+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] + num == 0:
                    triplets.append([num, nums[left], nums[right]])
                if nums[left] + nums[right] + num > 0:
                    right -= 1
                    continue
                if nums[left] + nums[right] + num < 0:
                    left += 1
                    continue
                left += 1
                right -= 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
                while nums[right] == nums[right+1] and left < right:
                    right -= 1
        return triplets