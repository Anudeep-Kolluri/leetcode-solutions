# Last updated: 7/21/2025, 1:01:14 AM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hl = len(haystack)
        nl = len(needle)

        # if nl == hl:
        #     return 0 if needle == haystack else -1

        for i in range(hl - nl + 1):
            if haystack[i : i+nl] == needle:
                return i
        
        return -1
        