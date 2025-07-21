# Last updated: 7/21/2025, 1:00:58 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if counter.get(i):
                counter[i] += 1
            else:
                counter[i] = 1
        
        Key, maxValue = 0, 0
        for key, value in counter.items():
            
            if value > maxValue:
                maxValue = value
                Key = key
        
        return Key
