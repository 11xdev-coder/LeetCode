def permuteUnique(nums: List[int]) -> List[List[int]]:
    # generate permutations with element skip
    nums.sort()
    n = len(nums)
    used = [False] * n

    ans = []
    current = []
    def dfs():
        if len(current) == n:
            ans.append(current[:])
            return

        for i in range(n):
            if used[i]:
                continue

            # if same num then:
            # if we are currently building this permutation, where first num is used, then dont skip
            # if we are on different branch and havent used it, then dont use the duplicate
            if i >= 1 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            current.append(nums[i])
            used[i] = True
            dfs()
            used[i] = False
            current.pop()

    dfs()
    return ans 

nums = list(map(int, input().split()))
print(permuteUnique(nums))
