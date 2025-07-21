# Last updated: 7/21/2025, 1:01:19 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)

        max_L = 0
        for i in range(len(s)-1):
            for j in range(i+1, len(s)+1):
                if j == len(s):
                    s_L = len(s[i:j])
                    if s_L > max_L:
                        max_L = s_L
                else:
                    substring = s[i:j]
                    #print(substring, s[j], i, j)
                    if s[j] in substring:
                        s_L = len(substring)
                        if s_L > max_L:
                            max_L = s_L
                        break

        
        return max_L
            