# Last updated: 7/21/2025, 1:01:07 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for i in nums:
            output += [k + [i] for k in output]

        return output