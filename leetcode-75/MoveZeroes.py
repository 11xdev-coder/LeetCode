
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 0
        while p1 < len(nums) and p2 < len(nums):
            if nums[p1] != 0:
                p1 += 1
            elif nums[p2] == 0 or p2 < p1:
                p2 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]                        
