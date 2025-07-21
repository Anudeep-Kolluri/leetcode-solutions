# Last updated: 7/21/2025, 1:01:03 AM
class Solution:
    def pascal(self, arr):
        if arr == []:
            return [1]

        if arr == [1]:
            return [1,1]

        output = []
        for i, j in zip(arr[:-1], arr[1:]):
            output.append(i+j)

        return [1] + output + [1]

    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []

        output = [[]]
        for i in range(numRows):
            output.append(self.pascal(output[-1]))
        
        return output[1:]
