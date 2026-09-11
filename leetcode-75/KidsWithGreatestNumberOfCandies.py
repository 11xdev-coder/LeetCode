class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max = max(candies)

        res = [False] * len(candies)
        for i, candie in enumerate(candies):
            if candie + extraCandies >= current_max:
                res[i] = True

        return res
