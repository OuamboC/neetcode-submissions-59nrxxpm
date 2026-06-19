class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Start left at 0
        left = 0
        # Start right at the end of the array
        right = len(numbers) - 1
        # Use a while loop where left < right
        while left < right:
            if numbers[left] + numbers[right] > target:
                # Decrease right to go inward
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                # Increase left
                left = left + 1
            else:
                return [left + 1, right + 1]
        return [left + 1, right + 1]
        
