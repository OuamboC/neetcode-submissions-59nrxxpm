class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = dict()
        for i in range(len(nums)):
            if target - nums[i] in result:
                return [result.get(target - nums[i]), i]
            else:
                result[nums[i]] = i
        return None
        