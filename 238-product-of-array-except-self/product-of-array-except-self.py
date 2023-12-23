class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preproduct = [1] * len(nums)
        postproduct = [1] * len(nums)
        result = [1] * len(nums)
        for index in range(len(nums)):
            if index == 0:
                preproduct[index] = 1
                continue
            preproduct[index] = preproduct[index - 1] * nums[index-1]
        print(preproduct)
        for index in range(len(nums)-1, -1, -1):
            if index == len(nums)-1:
                postproduct[index] = 1
                continue
            postproduct[index] = postproduct[index + 1] * nums[index+1]
        print(postproduct)
        for index in range(len(nums)):
            result[index] = preproduct[index]*postproduct[index]
        return result

                
            