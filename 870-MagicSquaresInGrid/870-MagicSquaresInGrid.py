# Last updated: 7/21/2025, 12:59:53 AM
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if (rows:=len(grid)) < 3 or (cols:=len(grid[0])) < 3:
            return 0


        ans = 0
        i,j = 0,0

        for i in range(rows - 2):
            for j in range(cols - 2):
                subgrid = [_[j:j+3] for _ in grid[i:i+3]]
                ans += self.checkSum(subgrid)
        
        return ans
        

        
    
    def checkSum(self, grid):
        out = set()
        nums = set()
        for i in range(3):
            rsum = 0
            csum = 0
            for j in range(3):
                rsum += grid[i][j]
                csum += grid[j][i]
                nums.add(grid[i][j])
            
            # print(rsum, csum)
            out.add(rsum)
            out.add(csum)
        
        out.add(grid[0][0] + grid[1][1] + grid[2][2])
        out.add(grid[0][2] + grid[1][1] + grid[2][0])

        req = set(range(1, 10))
        
        return 1 if len(out) == 1 and len(nums.intersection(req)) == 9 else 0