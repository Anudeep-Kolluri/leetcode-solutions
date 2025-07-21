# Last updated: 7/21/2025, 12:59:31 AM
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if arr == target:
            return True
        for idx, val in enumerate(target[:-1]):
            try:
                f = arr[idx:].index(val) + idx
                arr[idx : f+1] = arr[idx : f+1][::-1]
                # print(idx, f, arr, arr[idx : f+1][::-1])
            except:
                print("exception break")
                return False
            
        if target[-1] != arr[-1]:
            print(target[-1])
            return False
        
        return True