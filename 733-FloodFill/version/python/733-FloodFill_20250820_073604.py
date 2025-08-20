# Last updated: 8/20/2025, 7:36:04 AM
# Just like rotten oragnes
class Solution:
    def isValid(self, next_pos):
        x, y = next_pos
        

        c1 = x >= 0
        c2 = y >= 0
        c3 = x < self.m
        c4 = y < self.n

        if c1 and c2 and c3 and c4:
            return self.image[x][y] == self.start_color

        return False

    # def update(self, next_pos, curr_val):



    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        self.m, self.n = len(image), len(image[0])
        self.image = image
        self.start_color = image[sr][sc]
        
        start = (sr, sc)
        seen = set()
        queue = [start]
        
        image[sr][sc] = color

        while queue:

            curr = queue.pop(0)

            print(curr, queue)

            if curr in seen:
                continue
            
            seen.add(curr)
            x, y = curr

            # LEFT
            next_pos = (x, y-1)
            # print(next_pos, self.isValid(next_pos))
            if self.isValid(next_pos):
                if next_pos not in seen:
                    queue.append(next_pos)
                    image[next_pos[0]][next_pos[1]] = color

            # UP
            next_pos = (x-1, y)
            # print(next_pos, self.isValid(next_pos))
            if self.isValid(next_pos):
                if next_pos not in seen:
                    queue.append(next_pos)
                    image[next_pos[0]][next_pos[1]] = color


            # RIGHT
            next_pos = (x, y+1)
            # print(next_pos, self.isValid(next_pos))
            if self.isValid(next_pos):
                if next_pos not in seen:
                    queue.append(next_pos)
                    image[next_pos[0]][next_pos[1]] = color



            # DOWN
            next_pos = (x+1, y)
            # print(next_pos, self.isValid(next_pos))
            if self.isValid(next_pos):
                if next_pos not in seen:
                    queue.append(next_pos)
                    image[next_pos[0]][next_pos[1]] = color

        return image


        # print(self.isValid((0,0)))
        # print(self.isValid((-1,0)))
        # print(self.isValid((0,-1)))
        # print(self.isValid((-1,-1)))
        # print(self.isValid((self.m,0)))
        # print(self.isValid((0,self.m)))
        # print(self.isValid((self.n,0)))
        # print(self.isValid((0,self.n)))
        # print(self.isValid((self.m-1,self.n-1)))
        # print(self.isValid((self.n-1,self.m-1), 1))


        




            

        