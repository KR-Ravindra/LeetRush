class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            left, right = i+1, len(nums)-1
            while left<right:
                if nums[left] + nums[right] + nums[i] == 0 and left<right:
                    triplets.append([nums[left] , nums[right] , nums[i]])
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                    continue
                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                    continue
                left += 1
                right -= 1
                while nums[left] == nums[left-1] and left<right:
                    left += 1
                while nums[right] == nums[right+1] and left<right:
                    right -= 1
        return triplets
                