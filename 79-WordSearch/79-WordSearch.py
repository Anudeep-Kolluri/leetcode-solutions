# Last updated: 8/8/2025, 1:13:34 AM
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.m = len(board)
        self.n = len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(i, j, 0, set()):
                    return True
        return False

    def dfs(self, x: int, y: int, index: int, visited: set) -> bool:
        if index == len(self.word):
            return True
        
        if (x < 0 or x >= self.m or
            y < 0 or y >= self.n or
            (x, y) in visited or
            self.board[x][y] != self.word[index]):
            return False

        visited.add((x, y))
        
        # Explore 4 directions
        res = (
            self.dfs(x + 1, y, index + 1, visited) or
            self.dfs(x - 1, y, index + 1, visited) or
            self.dfs(x, y + 1, index + 1, visited) or
            self.dfs(x, y - 1, index + 1, visited)
        )
        
        visited.remove((x, y))  # backtrack
        return res
