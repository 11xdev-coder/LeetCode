def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()

    ans = set()
    for i in range(len(nums)):
        low, high = i+1, len(nums) - 1
        while low < high:
            s = nums[low] + nums[high] + nums[i]
            if s == 0:
                ans.add((nums[low], nums[high], nums[i]))
                low += 1
                high -= 1
            elif s < 0:
                low += 1
            else:
                high -= 1

    return list(ans)

nums = list(map(int, input().split())) 
print(threeSum(nums))


            
