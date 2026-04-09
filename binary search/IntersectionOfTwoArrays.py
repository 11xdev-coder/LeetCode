def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    # force nums1 to be smaller
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # perform binary search on larger array
    nums2.sort()

    res = []
    for num in nums1:
        low, high = 0, len(nums2) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums2[mid] == num:
                res.append(nums2[mid])
                break

            if nums2[mid] < num:
                low = mid + 1
            else:
                high = mid - 1

    return list(set(res))

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(intersection(nums1, nums2))
