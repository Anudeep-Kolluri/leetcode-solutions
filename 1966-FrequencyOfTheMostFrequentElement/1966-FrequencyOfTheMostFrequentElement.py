# Last updated: 7/21/2025, 12:58:09 AM
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        size = len(nums)

        l,r = 0,0
        freq = 0
        res = 0


        while r < size:
            freq += nums[r]


            while nums[r] * (r - l + 1) > freq + k:
                freq -= nums[l]
                l+=1
            
            res = max(res, r-l+1)
            r += 1
        
        return res

        