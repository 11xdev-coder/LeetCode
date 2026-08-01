def minimumTime(time: List[int], totalTrips: int) -> int:
    def can_do(min_time):
        s = 0
        for t in time:
            s += min_time // t

        return s >= totalTrips

    left, right = 1, max(time) * totalTrips
    while left <= right:
        mid = (left + right) // 2

        if can_do(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left

print(minimumTime(list(map(int, input().split())), int(input())))
