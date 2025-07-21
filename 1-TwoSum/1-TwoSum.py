# Last updated: 7/21/2025, 1:01:21 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return

        for idx, num in enumerate(nums[:-1]):
            if target - num in nums[idx+1:]:
                return [idx, nums[idx+1:].index(target-num)+idx+1]