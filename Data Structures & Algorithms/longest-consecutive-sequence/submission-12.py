class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Initialise longest sequence to 0
        longest_sequence = 0
        # Declare a set to save unique numbers
        result = set(nums)
        # Loop through result
        for num in result:
            # Check if previous number does not exist in result
            if num - 1 not in result:
                # Store current lenght
                current = 1
                # Start count sequence at num
                current_num = num 
                # Loop result until num + 1 exist in result
                while current_num + 1 in result:
                    # Update the lenght
                    current = current + 1
                    # Update count
                    current_num = current_num + 1
                # Get the longest sequence
                longest_sequence = max(longest_sequence, current)
        return longest_sequence
            
        