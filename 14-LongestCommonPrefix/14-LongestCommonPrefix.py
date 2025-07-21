# Last updated: 7/21/2025, 1:01:18 AM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return strs[0]

        word = strs[0]
        for i in strs[1:]:
            word = self.common(word, i)
            if not word:
                return ""
        
        return word


    

    def common(self, w1, w2):
        n = min(len(w1), len(w2))
        arr = [""] * n
        for idx, (_1, _2) in enumerate(zip(w1[:n], w2[:n])):
            if _1 == _2:
                arr[idx] = _1
            else:
                break
        
        return "".join(arr)