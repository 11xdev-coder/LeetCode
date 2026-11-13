from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q = deque(range(len(tickets)))
        t = 0
        while q and tickets[k] > 0:
            idx = q.popleft()
            tickets[idx] -= 1
            if tickets[idx] > 0:
                q.append(idx)
            t += 1

        return t
