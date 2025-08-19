# Last updated: 8/19/2025, 9:05:03 AM
# damn boi
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n_nodes = len(isConnected)
        seen = [0 for _ in range(n_nodes)]


        def dfs(node):

            if seen[node]:
                return
            
            seen[node] = 1

            nei = isConnected[node]
            # print(node, len(nei))
            for idx, n in enumerate(nei):
                if n == 1:
                    if idx == node:
                        continue
                    else:
                        dfs(idx)
        
        
        count = 0
        for i in range(n_nodes):
            if not seen[i]:
                count += 1
                dfs(i)

        return count

        