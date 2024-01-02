class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# solution:
# -> here space complexity is O(n); result array doesnt count.
# -> we compute prefix and postfix prodcut arrays; prefix array has at every index product of numbers from main nums array till index (not including index); similarly postfix has product till before that number from end of nums.
# -> for prefix we traverse nums from 0 to end; postfix we do it end to 0
# -> at last, for result array we multiply prefix[i]*postfix[i]
        # preproduct = [1] * len(nums)
        # postproduct = [1] * len(nums)
        # result = [1] * len(nums)
        # print(f"{preproduct=}{postproduct=}{result=}")
        # for index in range(len(nums)):
        #     if index == 0:
        #         continue
        #     preproduct[index] *= nums[index-1] * preproduct[index-1]
        # print(f"{nums=}{preproduct=}")
        # for index in range(len(nums)-1,-1,-1):
        #     if index == len(nums)-1:
        #         continue
        #     postproduct[index] = nums[index+1] * postproduct[index+1]
        # for index in range(len(nums)):
        #     result[index] *= preproduct[index] * postproduct[index]
        # return result

# with space complexity as O(1):
# -> instead of building two post and prefix arrays let us use variables and keep track of product and directly manipulate final array
# -> traversing remains same; during prefix sequence we go from 0 to end and at each index we have result as prefix and update prefix with current num for next; similarly for postfix sequence we do vice versa.. at each stage result is result*postfix and postfix equals postfix * current number
        prefix = 1
        postfix = 1
        result = [1]*len(nums)
        for index in range(1,len(nums),1):
            prefix *= nums[index-1]
            result[index] *= prefix

        for index in range(len(nums)-2, -1 , -1):
            postfix *= nums[index+1]
            result[index] *= postfix
        return result