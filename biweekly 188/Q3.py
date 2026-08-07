class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        def can_do(strength, diff):
            for i in range(len(monsters)):
                if strength < diff[i]: return False
                strength = max(strength - monsters[i], 0)

            return strength >= 0
        
        n = len(monsters)
        diffs = [0] * (n+1)
        diffs[0] = monsters[0]
        for i in range(1, n):
            diffs[i] = monsters[i] - monsters[i-1]

        for l, r, v in boosts:
            diffs[l] -= v
            diffs[r+1] += v

        res = []
        current = 0
        for i in range(n):
            current += diffs[i]
            res.append(current)

        left, right = 0, sum(monsters)
        while left <= right:
            mid = (left + right) // 2

            if can_do(mid, res):
                right = mid - 1
            else:
                left = mid + 1

        return left
