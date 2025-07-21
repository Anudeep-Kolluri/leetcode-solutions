# Last updated: 7/21/2025, 1:01:13 AM
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        output = ""
        string = self.countAndSay(n-1)
        counter = 0
        prev = string[0]
        for i in string:
            if i != prev:
                output += str(counter) + prev
                prev = i
                counter = 1
            else:
                counter += 1

        output += str(counter) + i
        
        return output