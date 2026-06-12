class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        while(left < right) :
            if (right - left) * min(heights[left], heights[right]) > max_water:
                max_water = (right - left) * min(heights[left], heights[right])
            elif heights[left] <= heights[right]:
                left = left + 1
            else:
                right = right - 1
        return max_water
           
            





        