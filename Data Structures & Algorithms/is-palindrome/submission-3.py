class Solution:
    def isPalindrome(self, s: str) -> bool:
        created = ""
        for char in s:
            if char.isalnum():
                created += char.lower()
        if created == created[::-1]:
            return True
        else:
            return False
        