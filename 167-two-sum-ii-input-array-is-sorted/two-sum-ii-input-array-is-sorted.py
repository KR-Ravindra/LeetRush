class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(numbers):
            if target-num in seen:
                print(f"{seen=} {target-num=} {num=}")
                return [ seen[target-num]+1,index+1]
            seen[num] = index    
        return 