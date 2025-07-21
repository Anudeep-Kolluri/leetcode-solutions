# Last updated: 7/21/2025, 1:01:09 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])