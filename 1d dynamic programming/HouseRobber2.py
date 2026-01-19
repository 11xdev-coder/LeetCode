# O(n) time, O(1) space
def robHelper(nums):
    if not nums:
        return 0

    second_last = 0
    last = 0
    
    res = 0
    for n in nums:
        res = max(last, second_last + n)
        second_last = last
        last = res
    return res

def rob(nums):
    N = len(nums)
    if N <= 1:
        return nums[0]
    
    # skip last or skip first
    return max(robHelper(nums[:-1]), robHelper(nums[1:]))

nums = list(map(int, input().split()))
print(rob(nums))
