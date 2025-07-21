# Last updated: 7/21/2025, 1:01:20 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return True if s[::-1] == s else False
        