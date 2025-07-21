# Last updated: 7/21/2025, 1:08:47 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True