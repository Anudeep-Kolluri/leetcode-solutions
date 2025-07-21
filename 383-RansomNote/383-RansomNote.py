# Last updated: 7/21/2025, 1:00:13 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for r in set(ransomNote):
            if ransomNote.count(r) > magazine.count(r):
                return False
        return True