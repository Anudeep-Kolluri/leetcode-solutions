# Last updated: 7/21/2025, 12:59:16 AM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        arr = [0] * len(nums)

        for idx, i in enumerate(nums):
            arr[idx] = nums[nums[idx]]
        
        return arr