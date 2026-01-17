
def rob(nums: List[int]) -> int:
    N = len(nums)
    if N <= 1:
        return nums[0]
    dp = [0] * N
 
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[N-1]

nums = list(map(int, input().split()))
print(rob(nums))
