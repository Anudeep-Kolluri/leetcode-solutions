# Last updated: 7/21/2025, 1:01:01 AM
class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.min) == 0 or self.min[-1] >= val:
            self.min.append(val)
        

    def pop(self) -> None:
        val = self.arr.pop()
        if self.min[-1] == val:
            self.min.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()