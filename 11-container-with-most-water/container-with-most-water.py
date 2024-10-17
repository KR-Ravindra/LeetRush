class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height)-1
        while left < right:
            current_area = (right - left)  * min(height[left], height[right])
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
                continue
            elif height[left] > height[right]:
                right -= 1
                continue
            else:
                left += 1
        return max_area