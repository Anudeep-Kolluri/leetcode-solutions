# Last updated: 7/21/2025, 1:00:11 AM
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        F = {r:str for r in range(15)}
        for i in range(3,15,3):
            F[i] = lambda _: "Fizz"
        for i in range(5,15,5):
            F[i] = lambda _: "Buzz"
        F[0] = lambda _: "FizzBuzz"
        return [F[i%15](i) for i in range(1,n+1)]