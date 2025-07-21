# Last updated: 7/21/2025, 1:00:12 AM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split(" ")

        # check 1 : both size = same
        if len(tokens) != len(pattern):
            return False
        
        # check 2 : mapping
        mapping = {}
        revMapping = {}
        for p, t in zip(pattern, tokens):
            if x:= mapping.get(p):
                if x != t:
                    return False
            else:
                if y:= revMapping.get(t):
                    return False

                mapping[p] = t
                revMapping[t] = p
        
        return True

        