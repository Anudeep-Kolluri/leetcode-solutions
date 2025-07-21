# Last updated: 7/21/2025, 1:00:14 AM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        if isBadVersion(n):
            if not isBadVersion(n-1):
                return n


        pu = n
        pl = 0
        m = int(round((pu + pl)/2))

        while True:
            if not isBadVersion(m):
                if isBadVersion(m+1):
                    return m+1
                #right
                pl = m

            else:
                
                #left
                pu = m

            m = int(round((pu + pl)/2))
