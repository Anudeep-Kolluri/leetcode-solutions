# Last updated: 7/21/2025, 1:01:14 AM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        pivot = end//2

        if target < nums[0]:
            return 0
        
        if target > nums[-1]:
            return end
        
        while pivot >= 0:
            print(pivot)
            if nums[pivot] == target:
                return pivot
            elif nums[pivot - 1] < target and nums[pivot] > target:
                return pivot
            elif nums[pivot] < target and nums[pivot + 1] > target:
                return pivot + 1
            elif nums[pivot] > target:
                #go left
                end = pivot
                pivot = round((start + end)/2)
            else:
                #go right
                start = pivot
                pivot = round((start + end)/2)