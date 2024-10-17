class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        result = []
        for a in range(len(nums)):
            if a>0 and sortedNums[a-1] == sortedNums[a]:
                continue
            left, right = a+1, len(nums)-1
            while left < right:
                if sortedNums[a] + sortedNums[left] + sortedNums[right] == 0:
                    result.append([sortedNums[a], sortedNums[left], sortedNums[right]])
                    left += 1
                    right -= 1
                    while sortedNums[left] == sortedNums[left-1] and left<right:
                        left += 1
                    while sortedNums[right] == sortedNums[right+1] and left<right:
                        right -= 1
                if sortedNums[a] + sortedNums[left] + sortedNums[right] < 0:
                    left += 1
                    continue
                if sortedNums[a] + sortedNums[left] + sortedNums[right] > 0:
                    right -= 1
                    continue
        return result
                