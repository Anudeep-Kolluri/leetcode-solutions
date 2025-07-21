# Last updated: 7/21/2025, 12:59:51 AM
class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        for i in range(n):
            a,b = a+b, a
        
        return a