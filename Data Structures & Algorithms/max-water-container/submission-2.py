class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_amount_water = 0
        while left < right:
            # Calculate the area
            if (right - left) * min(heights[left], heights[right]) > max_amount_water:
                max_amount_water = (right - left) * min(heights[left], heights[right])
            elif heights[left] <= heights[right]:
                left = left + 1
            else:
                right = right - 1
                
        return max_amount_water
        

        