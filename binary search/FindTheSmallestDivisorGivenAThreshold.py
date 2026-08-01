import math

def smallestDivisor(nums: List[int], threshold: int) -> int:
    def can_do(divisor):
        return sum(math.ceil(x / divisor) for x in nums) <= threshold

    left, right = 1, max(nums)
    while left <= right:
        mid = (left + right) // 2

        if can_do(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left

print(smallestDivisor(list(map(int, input().split())), int(input())))
