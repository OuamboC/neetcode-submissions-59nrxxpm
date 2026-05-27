class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()
        for i in range(len(nums)):
            result[nums[i]] = result.get(nums[i], 0) + 1
        sorted_key = sorted(result, key = lambda x: result[x], reverse = True)
        return sorted_key[:k]