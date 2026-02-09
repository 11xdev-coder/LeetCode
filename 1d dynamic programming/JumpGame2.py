def jump(nums: List[int]) -> int:
        N = len(nums)
        dp = [float('inf')] * N
        dp[0] = 0

        for i in range(N):
            num = nums[i]
            for j in range(num+1):
                new_pos = i + j
                if new_pos < N:
                    dp[new_pos] = min(dp[new_pos], dp[i] + 1)


        return dp[N-1]

nums = list(map(int, input().split()))
print(jump(nums))
