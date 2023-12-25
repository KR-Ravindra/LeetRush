class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
# solution with memory not constant
        # seen = {}
        # for index, num in enumerate(numbers):
        #     if target-num in seen:
        #         print(f"{seen=} {target-num=} {num=}")
        #         return [ seen[target-num]+1,index+1]
        #     seen[num] = index    
        # return 
# solution with memory constant
# -> using two pointers; since array is started, we will increase left if left+right < target; if left+right > target then we will decrease right.. as left to right values only increase.
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] > target:
                right -= 1
                continue
            if numbers[left] + numbers[right] < target:
                left += 1
                continue
        return False
    

            