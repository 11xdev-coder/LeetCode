def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    n = len(candidates)
    used = [False] * n

    ans = []
    current = []
    def dfs(start, remaining):
        if remaining == 0:
            ans.append(current[:])
            return

        if remaining < 0:
            return

        for i in range(start, n):
            if used[i]:
                continue

            if i >= 1 and candidates[i] == candidates[i-1] and not used[i-1]:
                continue

            current.append(candidates[i])
            used[i] = True
            dfs(i + 1, remaining - candidates[i])

            used[i] = False
            current.pop()

    dfs(0, target)
    return ans

nums = list(map(int, input().split()))
target = int(input())
print(combinationSum2(nums, target))
