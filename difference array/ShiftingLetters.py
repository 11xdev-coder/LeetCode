def shiftingLetters(s: str, shifts: List[int]) -> str:
    nums = [ord(x)-ord('a') for x in s]
    n = len(s)
    diff = [0] * (n+1)
    diff[0] = nums[0]
    for i in range(1, len(nums)):
        diff[i] = nums[i] - nums[i-1]

    for i, shift in enumerate(shifts):
        # l = 0, r = i, v = shift
        diff[0] += shift
        diff[i+1] -= shift

    result = []
    running = 0
    for num in diff:
        running += num
        result.append(running % 26)

    return "".join([chr(x + ord('a')) for x in result[:-1]])

s = input()
shifts = list(map(int, input().split()))
print(shiftingLetters(s, shifts))
