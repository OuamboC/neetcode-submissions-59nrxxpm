class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = dict()
        for c in s:
            result[c] = result.get(c, 0) + 1
        for c in t:
            if c in result:
                result[c] = result.get(c, 0) - 1
            else:
                return False
        return all(val == 0 for val in result.values())
            

        
    