# Last updated: 7/21/2025, 1:01:03 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a