# Last updated: 7/21/2025, 1:00:03 AM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)

        if flowerbed == [0]:
            return True


        for i in range(size-1):
            if i == 0 or i == size - 2:
                if flowerbed[i: i+2] == [0,0]:
                    count += 1
            else:
                if flowerbed[i:i+3] == [0,0,0]:
                    flowerbed[i+1] = 1
                    count += 1
        
        return True if count >= n else False