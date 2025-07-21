# Last updated: 7/21/2025, 12:59:16 AM
class Solution:

    def getLucky(self, s: str, k: int) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        hashmap = {}

        for idx, a in enumerate(alphabet):
            hashmap[a] = str(idx + 1)

        def ad(num):
            total = 0
            num = str(num)
            for i in num:
                total += int(i)
            return total
        
        num = ""
        for _ in s:
            num += hashmap[_]

        
        for i in range(k):
            num = ad(num)

        return num