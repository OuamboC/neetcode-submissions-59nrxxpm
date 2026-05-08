class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            #Step A: Put the current prefix in the result
            result[i] = prefix 
            # Step B: Update the prefix for the Next index
            prefix *= nums[i]

        suffix = 1
        # This range starts at the last index and goes to 0
        for i in range(len(nums) -1, -1, -1):
            # Multily the prefix already there by the suffix
            result[i] *= suffix
            # Update the suffix for the next number to the left
            suffix *= nums[i]
        return result
            
