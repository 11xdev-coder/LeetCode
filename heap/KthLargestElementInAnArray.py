import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = [-num for num in nums]
        heapq.heapify(h)

        ans = 0
        for _ in range(k):
            ans = -heapq.heappop(h)
        return ans
