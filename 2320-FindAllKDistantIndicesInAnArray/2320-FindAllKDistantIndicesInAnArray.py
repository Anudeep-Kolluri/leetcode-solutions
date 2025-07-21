# Last updated: 7/21/2025, 12:58:02 AM
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        found = [ idx for idx, i in enumerate(nums) if i == key]


        for idx, i in enumerate(nums):
            # 2 things
            # if idx - found[:] <= k and
            # nums[found[:]] == key
            for _ in found:
                if abs(idx - _ )<= k and nums[_] == key:
                    ans.append(idx)
                    break

        return ans