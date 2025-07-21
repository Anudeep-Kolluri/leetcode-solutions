# Last updated: 7/21/2025, 12:59:54 AM
class Solution:
    def recursion(self, n):
        out = []
        if n == self.size - 1:
            return [[n]]
        for idx, i in enumerate(self.paths[n]):
            x = self.recursion(i)
            for row in x:
                out.append([n]+row)
            print(out)
        return out
        

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.size = len(graph)
        self.paths = {}
        for idx, row in enumerate(graph):
            self.paths[idx] = row
        
        out = []

        for i in range(len(graph[0])):
            out.append(self.recursion(graph[0][i]))

        
        newOut = []

        for i in out:
            for j in i:
                if j[-1] != self.size - 1:
                    continue
                newOut.append([0] + j)

        return newOut