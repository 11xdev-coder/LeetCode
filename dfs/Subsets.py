def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)

    ans = [[]]
    current = []
    def dfs(start):
        # start - we cant take any idx BEFORE this idx
        # prevents duplicates, we dont need to store used nums
        for i in range(start, n):
            current.append(nums[i])
            ans.append(current[:]) # important: add a copy
            dfs(i+1) # start at the next one

            # back track
            current.pop()

    dfs(0)
    return ans

nums = list(map(int, input().split()))
print(subsets(nums))
