class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Declare empty dict
        result = {}
        # Loop through each word s in strs
        for s in strs:
            # compute the key from s
            key = tuple(sorted(s))
            # if key not in result, create result[key] = []
            if key not in result:
                result[key] = []
            # append s to result[key]
            result[key].append(s)
        # return values of result
        return list(result.values())
        
        
        
        

        