import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = list(range(1, n+1))
        ans = []
        for i in range(n, 0, -1):
            cnt = math.factorial(i-1) # amount in 1 sub group
            N = (k-1) // cnt
            ans.append(str(digits.pop(N)))
            k %= cnt
        return "".join(ans)
