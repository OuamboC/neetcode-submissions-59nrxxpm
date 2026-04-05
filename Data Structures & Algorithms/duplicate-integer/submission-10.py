class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers= set()
        for num in nums:
            if num not in unique_numbers:
                unique_numbers.add(num)
            else:
                return True
        return False


    
        
        