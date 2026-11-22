import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(h)

        ans = nums[:]
        for _ in range(k):
            ans[h[0][1]] = h[0][0] * multiplier
            heapq.heapreplace(h, (h[0][0] * multiplier, h[0][1]))

        return ans
