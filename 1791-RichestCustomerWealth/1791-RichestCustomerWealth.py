# Last updated: 7/21/2025, 12:59:26 AM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        out = 0
        for row in accounts:
            if (x := sum(row)) > out:
                out = x
        
        return out