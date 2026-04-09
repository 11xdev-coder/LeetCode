def findPeakElement(nums) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2

        left  = nums[mid-1] if mid - 1 >= 0 else float('-inf')
        right = nums[mid+1] if mid + 1 < len(nums) else float('-inf')

        if left < nums[mid] > right:
            return mid

        # a peak 100% exists if we continue going up
        # array eventually will start going down
        # and we will find the peak
        # we are on upward slope
        if nums[mid] < right:
            low = mid + 1
        else: # else the peak must be to the left
            high = mid - 1
            
nums = list(map(int, input().split()))
print(findPeakElement(nums))
