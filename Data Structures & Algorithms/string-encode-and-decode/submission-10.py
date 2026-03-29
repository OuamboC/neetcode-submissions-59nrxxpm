class Solution:

    def encode(self, strs: List[str]) -> str:
        result = list()
        if not strs:
            return ""
        for s in strs:
            list_of_ascii = list()
            for c in s:
                ascii = str(ord(c))
                list_of_ascii.append(ascii)
            new_string = " ".join(list_of_ascii)
            if not list_of_ascii:
                result.append("EMPTY")
            else:
                result.append(new_string)
        return "SEP".join(result)


    def decode(self, s: str) -> List[str]:
        # For each number before " ", convert to a get character
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
               

