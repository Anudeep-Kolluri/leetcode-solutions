# Last updated: 8/19/2025, 10:25:49 AM
from typing import List

class Solution:
    def boundCheck(self, pos):
        x, y = pos
        return (x < self.m) and (x >= 0) and (y < self.n) and (y >= 0)

    def convertGrid(self, grid):
        n_nodes = 1
        graph = {}
        rotten_nodes = []
        fresh_nodes = set()

        for idx1, i in enumerate(grid):
            for idx2, j in enumerate(i):
                if j == 1:
                    graph[n_nodes] = []
                    grid[idx1][idx2] = n_nodes
                    fresh_nodes.add(n_nodes)
                    n_nodes += 1
                elif j == 2:
                    graph[n_nodes] = []
                    grid[idx1][idx2] = n_nodes
                    rotten_nodes.append(n_nodes)
                    n_nodes += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]
                if curr:
                    # LEFT [0, -1]
                    next_pos = [i, j-1]
                    if self.boundCheck(next_pos):
                        if grid[next_pos[0]][next_pos[1]]:
                            graph[curr].append(grid[next_pos[0]][next_pos[1]])

                    # RIGHT [0, +1]
                    next_pos = [i, j+1]
                    if self.boundCheck(next_pos):
                        if grid[next_pos[0]][next_pos[1]]:
                            graph[curr].append(grid[next_pos[0]][next_pos[1]])

                    # UP [-1, 0]
                    next_pos = [i-1, j]
                    if self.boundCheck(next_pos):
                        if grid[next_pos[0]][next_pos[1]]:
                            graph[curr].append(grid[next_pos[0]][next_pos[1]])

                    # DOWN [+1, 0]
                    next_pos = [i+1, j]
                    if self.boundCheck(next_pos):
                        if grid[next_pos[0]][next_pos[1]]:
                            graph[curr].append(grid[next_pos[0]][next_pos[1]])

        return graph, n_nodes - 1, rotten_nodes, fresh_nodes

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        self.m, self.n = len(grid), len(grid[0])

        graph, n_nodes, rotten_nodes, fresh_nodes = self.convertGrid(grid)

        # No fresh oranges at all
        if not fresh_nodes:
            return 0

        # Fresh exist but no rotten to start the process
        if not rotten_nodes:
            return -1

        # Multi-source BFS starting from all rotten nodes
        queue = list(rotten_nodes)
        seen = [0] * (n_nodes + 1)
        for r in rotten_nodes:
            seen[r] = 1

        minutes = 0

        while queue:
            layer_size = len(queue)
            rotted_this_round = False

            for _ in range(layer_size):
                curr = queue.pop(0)
                for nei in graph[curr]:
                    # Only spread to fresh nodes
                    if nei in fresh_nodes:
                        fresh_nodes.remove(nei)
                        queue.append(nei)
                        seen[nei] = 1
                        rotted_this_round = True

            if rotted_this_round:
                minutes += 1
            else:
                break

        return minutes if not fresh_nodes else -1
