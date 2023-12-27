class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[len(height)-1]
        water_collected = 0
        left, right = 0, len(height)-1
        while left<right:
            print(f"{maxLeft=} {maxRight=}")
            if maxLeft < maxRight:
                left += 1
                if min(maxLeft, maxRight) - height[left] > 0:
                    print(f"Adding { min(maxLeft, maxRight) - height[left]} {height[left]=}")
                    water_collected +=  min(maxLeft, maxRight) - height[left]
                maxLeft = max(maxLeft, height[left])
            else:
                right -= 1
                if  min(maxLeft, maxRight) - height[right] > 0:
                    print(f"Adding { min(maxLeft, maxRight) - height[right]} {height[right]=}")
                    water_collected +=  min(maxLeft, maxRight) - height[right]
                maxRight = max(maxRight, height[right])
        return water_collected