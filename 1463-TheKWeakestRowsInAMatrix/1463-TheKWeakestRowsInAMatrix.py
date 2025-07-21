# Last updated: 7/21/2025, 12:59:34 AM
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = []
        for idx, row in enumerate(mat):
            count.append(row.count(1))

        n = list(range(len(count)))

        return sorted(n, key = lambda x : count[x])[:k]
