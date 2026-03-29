class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Declare empty hashmap
        result = {}
        # Loop through nums to get nums[i]
        for i in range(len(nums)):
            # If nums[i] not exist in result, add nums[i] to result
            if target - nums[i] in result:
                return [result.get(target - nums[i]), i]
            # If target - nums[i] exists in the dict, return the index of nums[i] and target - nums[i]
            else:
                result[nums[i]] = i
        return None
        
        
        
        



        
        
        