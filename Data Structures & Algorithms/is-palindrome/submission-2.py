class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [char.lower() for char in s if char.isalnum()]
        length = len(lst)
        mid = length // 2
        if length % 2 == 0:
            return lst[:mid] == lst[length:mid-1:-1]
        else:
            return lst[:mid] == lst[length:mid:-1]