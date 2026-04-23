def permute(nums: List[int]) -> List[List[int]]:
    # generate all subsets, but take only those with length N
    n = len(nums)
    used = [False] * n # keep track of used idx

    ans = []
    current = []
    def dfs():
        if len(current) == n:
            ans.append(current[:])
            return

        for i in range(n):
            if used[i]:
                continue

            current.append(nums[i])
            used[i] = True
            dfs() # try adding nums further

            # back track
            used[i] = False
            current.pop()

    dfs()
    return ans

nums = list(map(int, input().split()))
print(permute(nums))
