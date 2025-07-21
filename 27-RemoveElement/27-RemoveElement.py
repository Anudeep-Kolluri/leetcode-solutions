# Last updated: 7/21/2025, 1:01:15 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
                nums[i] = 100
        
        nums.sort()
        
        return len(nums) - count