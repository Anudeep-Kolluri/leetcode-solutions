# Last updated: 7/21/2025, 1:01:17 AM
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
      self.stack.append(n)

    def pop(self):
      return self.stack.pop()

    def values(self):
        return self.stack

    def top(self):
        return self.stack[-1]

class Solution:
    def isValid(self, s: str) -> bool:
        combinations = {
            ")" : "(",
            "]" : "[",
            "}" : "{",

        }

        if s == "":
            return False
        
        if len(s) % 2 == 1:
            return False

        stack = Stack()
        pointer = 0
        size = len(s)

        while pointer < size:
            if not stack.values():
                stack.push(s[pointer])
            else:
                if stack.top() == combinations.get(s[pointer]):
                    stack.pop()
                else:
                    stack.push(s[pointer])
            
            pointer += 1

        print(stack.values())
        return False if stack.values() else True