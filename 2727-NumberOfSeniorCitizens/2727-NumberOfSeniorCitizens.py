# Last updated: 7/21/2025, 12:58:01 AM
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return reduce(lambda a, b : a+b, [1 if (int(record[11] + record[12])) > 60 else 0 for record in details])