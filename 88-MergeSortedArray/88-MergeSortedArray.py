# Last updated: 7/21/2025, 1:01:06 AM
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        if n == 0:
            return
        
        if m == 0:
            nums1[:] = nums2
            return

        #merge sort maybe?
        a1 = nums1[:m]
        a2 = nums2[:n]

        nums1[:] = self.sort(a1, a2)

    
    def sort(self, a1, a2):
        l1 = len(a1)
        l2 = len(a2)
        if l1 == 0 or l2 == 0:
            return a1 + a2
        elif l1 == 1 and l2 == 1:
            return a1 + a2 if a1[0] < a2[0] else a2 + a1
        
        mid1 = l1//2
        left = self.sort(a1[:mid1], a1[mid1:])

        mid2 = l2//2
        right = self.sort(a2[:mid2], a2[mid2:])

        ans = []
        while left and right:
            if left[0] < right[0]:
                ans.append(left.pop(0))
            else:
                ans.append(right.pop(0))
        if left:
            ans += left
        if right:
            ans += right

        return ans