class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()
        for num in nums:
            result[num] = result.get(num, 0) + 1
        sorted_keys = sorted(result, key = lambda x: result[x], reverse = True)
        return sorted_keys[:k]
        