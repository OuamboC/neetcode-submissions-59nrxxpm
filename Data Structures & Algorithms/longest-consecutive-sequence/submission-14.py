class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        result = set(nums)
        for num in result:
            if num - 1 not in result:
                current = 1
                current_num = num
                while current_num + 1 in result:
                    current += 1
                    current_num += 1
                longest_sequence = max(longest_sequence, current)
        return longest_sequence
        