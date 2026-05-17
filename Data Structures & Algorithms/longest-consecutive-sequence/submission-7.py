class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        result = set()
        for num in nums:
            result.add(num)
        for num in result:
            if num - 1 not in result:
                current = 1
                length = num
                while length + 1 in result:
                    length = length + 1
                    current = current + 1
                longest_sequence = max(longest_sequence, current)
        return longest_sequence



        