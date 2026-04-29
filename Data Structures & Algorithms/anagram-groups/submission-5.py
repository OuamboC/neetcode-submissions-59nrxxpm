class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Declare an empty dictionnary
        result = dict()
        # Loop through strs
        for s in strs:
            # Compute key to s
            key = tuple(sorted(s))
            # Check if key in result
            if key not in result:
                result[key] = []
            result[key].append(s)
        return list(result.values())



        