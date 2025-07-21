# Last updated: 7/21/2025, 1:00:10 AM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans = ans ^ i
        
        return ans