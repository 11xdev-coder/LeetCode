
class Solution:
    def maxArea(self, h: list[int]) -> int:
        if len(h) == 2:
            return min(h[0], h[1])

        ans = 0
        l, r = 0, len(h)-1
        while l < r:
            ans = max(ans, min(h[l],h[r]) * (r - l))
            if h[l] < h[r]:
                l+=1
            else:
                r-=1

        return ans
