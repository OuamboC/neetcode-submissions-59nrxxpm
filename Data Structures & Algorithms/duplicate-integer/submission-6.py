class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set()
        for i in range(len(nums)):
            if nums[i] in unique_numbers:
                return True
            else:
                unique_numbers.add(nums[i])
        return False
        