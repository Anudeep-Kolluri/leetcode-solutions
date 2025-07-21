# Last updated: 7/21/2025, 12:59:56 AM
class Solution:
    def __init__(self):
        #self.q = Queue()
        self.X = 0
        self.Y = 0
        self.cc = 0
        self.nc = 0

        self.map = {
            0 : (-1, 0),
            1 : (1, 0),
            2 : (0, -1),
            3 : (0, 1),
        }


    def left(self, x, y):
        #Go up
        step = y-1
        if step < 0:
            return False

        if self.visited[x][step]:
            return False

        if self.image[x][step] == self.cc:
            self.image[x][step] = self.nc
            self.visited[x][step] = 1
            return True
        else:
            return False


    def right(self, x, y):
        #Go down
        step = y+1
        if step >= self.X:
            return False

        if self.visited[x][step]:
            return False
        
        if self.image[x][step] == self.cc:
            self.image[x][step] = self.nc
            self.visited[x][step] = 1
            return True
        else:
            return False

    
    def up(self, x, y):
        #Go left
        step = x-1
        if step < 0:
            return False

        if self.visited[step][y]:
            return False
        
        if self.image[step][y] == self.cc:
            self.image[step][y] = self.nc
            self.visited[step][y] = 1
            return True
        else:
            return False

    

    def down(self, x, y):
        #Go right
        step = x+1
        if step >= self.Y:
            return False

        if self.visited[step][y]:
            return False
        
        if self.image[step][y] == self.cc:
            self.image[step][y] = self.nc
            self.visited[step][y] = 1
            return True
        else:
            return False

    
    def fill(self, x, y):
        up = self.up(x, y)
        down = self.down(x, y)
        left = self.left(x,y)
        right = self.right(x,y)

        return (up, down, left, right)


    def answer(self, x, y):
        filledTuple = self.fill(x,y)
        print(filledTuple)
        if filledTuple == (False, False, False, False):
            #All filled in that position
            return
        
        for idx, i in enumerate(filledTuple):
            if i:
                #self.q.push(self.map[idx])
                xx, yy = self.map[idx]
                self.answer(x + xx, y + yy)


    def floodFill(self, image, sr: int, sc: int, color: int):
        self.image = image
        self.sr = sr
        self.sc = sc
        self.cc = image[sr][sc]
        self.nc = color

        self.X = len(image[0])
        self.Y = len(image)

        self.image[sr][sc] = self.nc

        self.visited = [[0 for i in range(self.X)] for j in range(self.Y)]
        self.visited[sr][sc] = 1

        self.answer(sr, sc)

        return self.image
        