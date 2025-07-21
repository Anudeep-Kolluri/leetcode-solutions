# Last updated: 7/21/2025, 12:59:53 AM
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        z = 0
        for j in range(len(strs[0])):
            for k in range(len(strs)):
                print(strs[k][j], ord(strs[k][j]), z)
                n = ord(strs[k][j])
                if n < z:
                    count += 1
                    print("I am here")
                    break
                z = n
            z = 0

        return count