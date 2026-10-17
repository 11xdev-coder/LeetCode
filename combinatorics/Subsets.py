class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        c = []

        def dfs(i):
            ans.append(c[:])

            for i in range(i, len(nums)):
                c.append(nums[i])
                dfs(i+1)
                c.pop()

        dfs(0)
        return ans
