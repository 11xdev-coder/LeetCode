import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        h = []
        cnt = Counter(words)

        for key, value in cnt.items():
            heapq.heappush(h, (-value, key))

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(h)[1])

        return ans
