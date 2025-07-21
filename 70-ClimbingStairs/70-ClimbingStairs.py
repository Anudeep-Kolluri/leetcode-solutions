# Last updated: 7/21/2025, 1:01:09 AM
class Solution:
    def fibo(self,n):
        a,b = 1,1
        for i in range(n):
            a,b = a+b, a
        return b

    def climbStairs(self, n: int) -> int:
        return self.fibo(n)