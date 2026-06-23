class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for char in list(s.lower()):
            if char.isalnum():
                palindrome += char
        return palindrome == palindrome[::-1]