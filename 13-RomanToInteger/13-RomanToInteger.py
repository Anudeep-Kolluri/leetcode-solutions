# Last updated: 7/21/2025, 1:01:18 AM
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        if len(s) == 1:
            return values[s]

        res = 0
        for idx, i in enumerate(s[:-1]):
            val1 = values[s[idx]]
            val2 = values[s[idx+1]]
            if val2 > val1:
                res -= val1
            elif val1 > val2:
                res += val1
            else:
                res += val1
        
        return res + val2