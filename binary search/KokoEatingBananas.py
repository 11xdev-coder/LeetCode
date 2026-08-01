import math

def can_do(piles, h, k):
    cnt = 0
    for p in piles:
        cnt += math.ceil(p / k)
    return cnt <= h

def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    while left <= right:
        mid = (left + right) // 2

        if can_do(piles, h, mid):
            right = mid - 1
        else:
            left = mid + 1

    return left

print(minEatingSpeed(list(map(int, input().split())), int(input())))
