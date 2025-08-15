# Last updated: 8/15/2025, 7:32:45 AM
class Solution:

    def boundCheck(self, pos):
        if pos[0] < 0 :
            return False
        
        if pos[1] < 0:
            return False

        if pos[0] >= self.rows:
            return False

        if pos[1] >= self.cols:
            return False

        return True

    def markGrid(self, pos):
        self.visited_grid[pos[0]][pos[1]] = True

    def checkGrid(self, pos):
        return not self.visited_grid[pos[0]][pos[1]]

    def sameChar(self, pos, char):
        return self.grid[pos[0]][pos[1]] == char

    def findNextUnvisited(self):
        for idx1, _ in enumerate(self.visited_grid):
            for idx2, __ in enumerate(_):
                if not __:
                    return ([idx1, idx2], self.grid[idx1][idx2])

        return None

    def isValid(self, pos, char):
        is_inbound = self.boundCheck(pos)
        if is_inbound:
            is_same_char = self.sameChar(pos, char)
        return is_inbound and is_same_char

    def shiftSeen(self, next_pos):
        self.seen[0] = self.seen[1]
        self.seen[1] = self.seen[2]
        self.seen[2] = next_pos


    def containsCycle(self, grid: List[List[str]]) -> bool:

        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])

        visited = [[False]*self.cols for _ in range(self.rows)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        for sr in range(self.rows):
            for sc in range(self.cols):
                if visited[sr][sc]:
                    continue

                ch = grid[sr][sc]
                # stack items: (r, c, pr, pc) where (pr, pc) is parent
                stack = [(sr, sc, -1, -1)]
                visited[sr][sc] = True

                while stack:
                    r, c, pr, pc = stack.pop()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols and grid[nr][nc] == ch:
                            if not visited[nr][nc]:
                                visited[nr][nc] = True
                                stack.append((nr, nc, r, c))
                            else:
                                # neighbor is visited already
                                if not (nr == pr and nc == pc):
                                    return True
        return False


