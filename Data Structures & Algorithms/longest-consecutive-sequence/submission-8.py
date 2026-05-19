class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Assume that longest_sequence is 0
        longest_sequence = 0
        # Create a result to store unique numbers in nums
        result = set()
        # Loop through noms to populate result
        for num in nums:
            result.add(num)
        # Loop through each num in result
        for num in result:
            # Check if num - 1 not in result
            if num - 1 not in result:
                # Declare the lenght of longest sequence is 1
                current = 1
                # Declare lenght as being num 
                length = num
                # Loop longest sequence until num + 1 exist
                while length + 1 in result:
                    # State that lenght increase by one 
                    length = length + 1
                    # Update the current lenght
                    current = current + 1
                # Find the greatest lenght
                longest_sequence = max(longest_sequence, current)
        return longest_sequence
    
        
           

        