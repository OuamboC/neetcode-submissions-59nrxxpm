class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Declare the longest_sequence to 0
        longest_sequence = 0
        # Create result to store unique numbers
        result = set(nums)
        # Loop through result 
        for num in result:
            # Check that num - 1 do not exist
            if num - 1 not in result:
                # Get the length of the current sequence
                current = 1
                # Start a sequence with with the current number 
                current_num = num
                # Loop result until num + 1 exist 
                while current_num + 1 in result:
                    # Update the length
                    current +=1
                    # Update the current number
                    current_num +=1
                # Get the max length
                longest_sequence = max(longest_sequence, current)
        return longest_sequence
