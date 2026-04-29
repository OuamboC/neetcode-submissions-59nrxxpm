class Solution:

    def encode(self, strs: List[str]) -> str:
        # Declare empty list to result
        result = list()
        # If strs is empty return empty string
        if not strs:
            return ""
        # Loop through strs to find each string
        for s in strs:
            # Declare empty list to store all ascii
            list_of_ascii = list()
            # Loop through each character to convert to ASCII
            for c in s:
                ascii = str(ord(c))
                # Store ascii in list_of_ascii
                list_of_ascii.append(ascii)
                # Declare new_string to create a new string of list_of_ascii
            new_string = " ".join(list_of_ascii)
            if not list_of_ascii:
                result.append("EMPTY")    
            else:
                result.append(new_string)    
        return "SEP".join(result)

    def decode(self, s: str) -> List[str]:
        result = list()
        if not s:
            return []
        s = s.split("SEP")
        for string in s:
            if string.strip() == "EMPTY":
                result.append("")
                continue
            new_string = list()
            for ascii_word in string.strip().split(" "):
                if ascii_word:
                    character = chr(int(ascii_word))
                    new_string.append(character)
            result.append("".join(new_string))
        return result
            

