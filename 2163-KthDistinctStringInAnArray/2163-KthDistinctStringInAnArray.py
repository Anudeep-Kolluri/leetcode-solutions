# Last updated: 7/21/2025, 12:58:03 AM
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = {}
        for i in arr:
            if counter.get(i):
                counter[i] += 1
            else:
                counter[i] = 1
        
        rev = {}
        count = 0
        for key, item in counter.items():
            if item == 1:
                count += 1
                if count == k:
                    return key
        
        return ""