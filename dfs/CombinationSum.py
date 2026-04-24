def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    n = len(candidates)

    ans = []
    current = []
    def dfs(start, remaining):
        if remaining == 0:
            ans.append(current[:])
            return

        if remaining < 0:
            return

        for i in range(start, n):
            current.append(candidates[i])
            dfs(i, remaining - candidates[i])
            current.pop()

    dfs(0, target)
    return ans

nums = list(map(int, input().split()))
target = int(input())
print(combinationSum(nums, target))
