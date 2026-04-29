class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()
        for i in range(len(nums)):
            result[nums[i]] = result.get(nums[i],0) + 1
            sorted_keys = sorted(result, key = lambda x: result[x], reverse = True)
        return sorted_keys[:k]

        