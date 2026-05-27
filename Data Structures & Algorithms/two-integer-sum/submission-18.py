class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Declare a dict to store nums
        result = dict()
        # Loop through nums
        for i in range(len(nums)):
            # Check if target - nums[i] in result 
            if target - nums[i] in result:
                return [result.get(target - nums[i]), i]
            else:
                result[nums[i]] = i
        pass
        