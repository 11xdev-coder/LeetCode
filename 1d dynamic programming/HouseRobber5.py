def rob(nums: List[int], colors: List[int]) -> int:
    N = len(nums)
    if N <= 1:
        return nums[0]
    dp = [0] * N
        
    # base
    # for first index -> we always choose first and only number
    # for second index we have a choice
    # 1. if colors are different, then we can rob both indexes (nums[0] + nums[1])
    # 2. if color is the same, we can't rob them, therefore we choose the maximum
    dp[0] = nums[0] 
    dp[1] = (nums[0] + nums[1]) if colors[0] != colors[1] else max(nums[0], nums[1])

    for i in range(2, N):
        # for every house we can choose:
        # 1. skip it -> choosing maximum of 2 previous robs
        # 2. rob it -> we can only rob adjacent houses (dp[i-1]) if their colors are different (colors[i] != colors[i-1])
        # we select the option that yields maximum amount
        skip = max(dp[i-1], dp[i-2])
        rob = nums[i] + max(dp[i-1] if colors[i] != colors[i-1] else -1, dp[i-2])
        dp[i] = max(rob, skip)

    return dp[-1]

houses = list(map(int, input().split()))
colors = list(map(int, input().split()))
print(rob(houses, colors))
