# Last updated: 7/21/2025, 1:01:12 AM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        arr = sorted(candidates)

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i == len(arr):
                return

            
            cur.append(arr[i])
            dfs(i+1, cur, total + arr[i])
            cur.pop()

            while i + 1 < len(arr) and arr[i] == arr[i+1]:
                i+=1
            
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res