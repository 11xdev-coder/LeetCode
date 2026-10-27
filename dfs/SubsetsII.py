class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans, cur = [], []
        def dfs(start):
            ans.append(cur[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                cur.append(nums[i])
                dfs(i+1)
                cur.pop()

        dfs(0)
        return ans                
