# Last updated: 7/21/2025, 12:58:07 AM

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        output = [[]]

        for i in nums:
            output += [k + [i] for k in output]


        out = 0
        for i in output:
            tmp = 0
            for j in i:
                tmp ^= j

            out += tmp

        return out
        