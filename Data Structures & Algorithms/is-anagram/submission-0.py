class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Declare empty dict
        result = {}
        # Loop through s to get each character
        for c in s:
            # Add all characters of s in dict and count the iteration of each characters 
            result[c]= result.get(c,0) +1
        # Loop through t to get each character
        for c in t:
            # Check if char in t already in dict and count[char[s]] == count[char[t]]
            if c in result :
                result[c] = result.get(c,0) -1
            else:
                return False
        return all(val == 0 for val in result.values())
        
        
        
        