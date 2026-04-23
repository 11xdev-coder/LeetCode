def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)

    # rightmost element at i, that nums[i] < nums[i+1]
    i = n - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    # if no such element found, i = -1
    # for example, [3, 2, 1] we will need to just reverse -> [1. 2. 3]

    if i >= 0:
        # rightmost element at j, nums[j] > nums[i]
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        # swap
        nums[i], nums[j] = nums[j], nums[i]

    # reverse everything after i
    nums[i+1:] = nums[i+1:][::-1]

nums = list(map(int, input().split()))
nextPermutation(nums)
print(nums)
