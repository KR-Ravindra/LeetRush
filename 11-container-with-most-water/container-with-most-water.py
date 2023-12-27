class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        # for left in range(1,len(height)+1):
        #     for right in range(len(height), left, -1):
        #         area = (right - left) * min(height[left-1],height[right-1])
        #         max_area = max(max_area, area)
        #         # print(f"{right-left=} {min(height[left-1],height[right-1])=} {area=} {max_area=}")
        # return max_area
        left, right = 0, len(height)-1
        while left<right:
            less_height = min(height[left],height[right])
            area = less_height * (right-left)
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area