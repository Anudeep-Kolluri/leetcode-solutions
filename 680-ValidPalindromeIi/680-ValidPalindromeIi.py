# Last updated: 7/21/2025, 12:59:56 AM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        rev = s[::-1]

        if s == rev:
            return True

        for idx, (correct, reverse) in enumerate(zip(s, rev)):
            if correct != reverse:
                break

        l1 = s[:idx]
        r1 = s[idx+1:]

        word1 = l1+r1

        l2 = rev[:idx]
        r2 = rev[idx+1:]

        word2 = l2+r2

        return True if (word1 == word1[::-1]) or (word2 == word2[::-1]) else False
