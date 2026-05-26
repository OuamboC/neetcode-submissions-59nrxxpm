class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Declare a dictionnary to store strings with similar letters 
        result = defaultdict(list)
        # Loop through each string in strs 
        for s in strs:
            # Compute key to tuple while sorting s 
            key = tuple(sorted(s))
            # Add the the sorted s to key
            result[key].append(s)
        # Return the list of values of result
        return list(result.values())
        