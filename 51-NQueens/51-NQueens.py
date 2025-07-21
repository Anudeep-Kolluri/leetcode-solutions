# Last updated: 7/21/2025, 1:01:11 AM
import copy
# SUBMITTED USING CHATGPT
#
# THIS IS THE ACTUAL CODE I WROTE

import copy

# class Solution:


#     def _isvalid(self, pos):
#         return True if '.' in self.valid[pos[0]][pos[1]] else False
    
    
#     def _updateValid(self, pos):
#         r,c = pos
#         _r1, _c1 = pos
#         half = (self.n // 2) + 1 if self.n % 2 == 1 else self.n // 2


#         if r > c:
#             _r1 = r - c
#             _c1 = 0
#         else:
#             _r1 = 0
#             _c1 = c - r

#         if r > half or c > half:
#             _c2 = self.n - 1
#             _r2 = r - (self.n - c - 1)
#         else:
#             _r2 = 0
#             _c2 = c + r

#             if _c2 == self.n:
#                 _c2 -= 1



#         for _ in range(self.n):
#             self.valid[r][_] = 'x'  #update Horizontal
#             self.valid[_][c] = 'x'  #update Vertical

#             if _r1 < self.n and _c1 < self.n:   #update Left Diagonal
#                 self.valid[_r1][_c1] = 'x'
#                 _r1 += 1
#                 _c1 += 1

#             if _r2 < self.n and _c2 >= 0:       #update Right Diagonal
#                 # print('r2, c2', _r2, _c2)     # BUG PRESENT HERE
#                 self.valid[_r2][_c2] = 'x'          
#                 _r2 += 1
#                 _c2 -= 1
            


#     def insertQueen(self, pos):
#         r,c = pos
#         # if self._isvalid(pos):
#         self.board[r][c] = 'Q'
#         self._updateValid(pos)




#     def printBoard(self, board):
#         print("\n".join(list(map(lambda x : " | ".join(x), board))))
    

#     def solveNQueens(self, n: int):

#         self.n = n
#         self.board = [['.']*n for _ in range(n)]
#         self.valid = [['.']*n for _ in range(n)]
        
#         # stack = []

#         def moveNext(pos):
#             r, c = pos
#             if c < self.n-1:
#                 c = c+1
#             else:
#                 c = 0
#                 r += 1
#             return (r, c)



#         def solve(pos, queensPlaced = 0):
#             # print(pos)

#             placed = False
#             copyoriginal = copy.deepcopy(self.board)
#             copyvalid = copy.deepcopy(self.valid)

#             if queensPlaced == self.n:
#                 print("Solution found")
#                 return True
            
#             if self._isvalid(pos):
#                 self.insertQueen(pos)
#                 queensPlaced += 1
#                 placed = True
#                 # self.printBoard(boardcopyorignal)
#                 # self.printBoard(boardcopyvalid)
#                 # print()
#                 # print(queensPlaced)
            
#             pos = moveNext(pos)

#             if pos[0] == self.n:
#                 if queensPlaced == self.n:
#                     return True
#                 return False
            
#             if not solve(pos, queensPlaced) and moveNext(pos)[0] != self.n:
#                 if placed:
#                     print(pos)
#                     queensPlaced -= 1
#                     self.board = copyoriginal
#                     self.valid = copyvalid

#                     self.printBoard(self.board)
#                     self.printBoard(self.valid)
#                     print()
#                     # self.printBoard()
#                     solve(pos, queensPlaced)



#         solve((0, 1))





# n = 4

# game = Solution()
# game.solveNQueens(n)
# print()
# # while True:
# #     pos = (int(input()), int(input()))
# #     game.insertQueen(pos)
# #     game.printBoard()
# #     game.printBoard(True)

#
#
#
class Solution:
    def _isvalid(self, pos):
        r, c = pos
        return self.valid[r][c] == '.'
    
    def _updateValid(self, pos):
        r, c = pos
        n = self.n
        # mark row and column
        for i in range(n):
            self.valid[r][i] = 'x'
            self.valid[i][c] = 'x'
        # mark left diagonal (top-left to bottom-right)
        i = r - min(r, c)
        j = c - min(r, c)
        while i < n and j < n:
            self.valid[i][j] = 'x'
            i += 1
            j += 1
        # mark right diagonal (top-right to bottom-left)
        i = r - min(r, n - c - 1)
        j = c + min(r, n - c - 1)
        while i < n and j >= 0:
            self.valid[i][j] = 'x'
            i += 1
            j -= 1

    def insertQueen(self, pos):
        r, c = pos
        self.board[r][c] = 'Q'
        self._updateValid(pos)

    def printBoard(self, board):
        print("\n".join(" | ".join(row) for row in board))
    
    def solveNQueens(self, n: int):
        self.n = n
        self.board = [['.'] * n for _ in range(n)]
        self.valid = [['.'] * n for _ in range(n)]
        solutions = []
        
        def backtrack(row):
            if row == n:
                solutions.append(copy.deepcopy(self.board))
                return
            for col in range(n):
                if self.valid[row][col] == '.':
                    # backup state
                    board_backup = copy.deepcopy(self.board)
                    valid_backup = copy.deepcopy(self.valid)
                    
                    self.insertQueen((row, col))
                    backtrack(row + 1)
                    
                    # backtrack
                    self.board = board_backup
                    self.valid = valid_backup
        
        backtrack(0)
        if solutions:
            print("Solution(s) found:")
            self.printBoard(solutions[0])
        else:
            print("No solution found.")
        return list(map(lambda sol: list(map(lambda x: "".join(x), sol)), solutions))