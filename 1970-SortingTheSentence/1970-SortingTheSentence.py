# Last updated: 7/21/2025, 12:58:08 AM
class Solution:
    def sortSentence(self, s: str) -> str:
        tokens = s.split(" ")
        sentence = [""]*len(tokens)
        for t in tokens:
            sentence[int(t[-1])-1] = t[:-1]
        return " ".join(sentence)