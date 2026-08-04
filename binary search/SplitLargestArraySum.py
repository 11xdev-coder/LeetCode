def splitArray(nums: List[int], k: int) -> int:
    def can_do(max_sum):
        splits = 0
        s = 0
        for n in nums:
            s += n
            if s > max_sum:
                s = n
                splits += 1

        return splits <= k - 1

    left, right = max(nums), sum(nums)
    while left <= right:
        mid = (left + right) // 2

        if can_do(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


print(splitArray(list(map(int, input().split())), int(input())))
