# Last updated: 7/21/2025, 1:01:08 AM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        #insertion sort
        for i in range(n-1):
            k = i
            while nums[k+1] < nums[k]:
                nums[k+1], nums[k] = nums[k], nums[k+1]
                k-=1
                if k < 0:
                    k = 0
            print("====")
        