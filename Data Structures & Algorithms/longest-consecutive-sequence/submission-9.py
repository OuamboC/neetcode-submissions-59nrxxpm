class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Assume that longest_sequence is 0
        longest_sequence = 0
        # Create a result to store unique numbers in nums
        result = set(nums)
        # Loop through each num in result
        for num in result:
            # Only start counting from the beginning of a sequence
            if num - 1 not in result:
                # Declare the current count as 1
                current = 1
                # Start walking from the beginning of this sequence
                current_num = num
                # Loop longest sequence until num + 1 exist
                while current_num + 1 in result:
                    # State that length increase by one 
                    current_num = current_num + 1
                    # Update the current count
                    current = current + 1
                # Find the greatest length
                longest_sequence = max(longest_sequence, current)
        return longest_sequence
    
        
           

        