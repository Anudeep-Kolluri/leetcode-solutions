# Last updated: 7/21/2025, 12:59:50 AM
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(i) for i in str(int("".join(map(str, num))) + k)]