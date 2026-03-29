class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set(nums)

        return len(unique_numbers) != len(nums)
            