class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        #Pass 1: Left to Right (prefixes)
        prefix = 1
        for i in range(n):
            #Step A: Put the current prefix in the result
            result[i] = prefix 
            # Step B: Update the prefix for the Next index
            prefix *= nums[i]

        #Pass 2: Right to left (Suffixes)
        suffix = 1
        # This range starts at the last index and goes to 0
        for i in range(n -1, -1, -1):
            # Multily the prefix already there by the suffix
            result[i] *= suffix
            # Update the suffix for the next number to the left
            suffix *= nums[i]
        return result
            




