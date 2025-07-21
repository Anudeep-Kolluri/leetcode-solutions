# Last updated: 7/21/2025, 12:58:01 AM
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if not derived or len(derived) < 1:
            return True

        xor = lambda a,b : 1 if a != b else 0
        
        arr = [0]

        for idx, i in enumerate(derived[:-1]):
            if (i == 1 and arr[idx] == 0) or (i == 0 and arr[idx] == 1):
                arr.append(1)
            else:
                arr.append(0)
        
        print(arr)

        return True if xor(arr[0], arr[-1]) == derived[-1] else False