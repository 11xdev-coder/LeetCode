def can_do(weights, days, cap):
    s = 0
    cnt = 1
    for w in weights:
        if s + w > cap:
            s = 0
            cnt += 1
        s += w
        
    return cnt <= days

def shipWithinDays(weights: List[int], days: int) -> int:
    left, right = max(weights), sum(weights)
    while left <= right:
        mid = (left + right) // 2

        if can_do(weights, days, mid):
            right = mid - 1
        else:
            left = mid + 1

    return left

print(shipWithinDays(list(map(int, input().split())), int(input())))
