def intToRoman(num: int) -> str:
    vals = [1000, 500, 100, 50, 10, 5, 1]
    romans = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    res = []

    s = str(num)
    for i in range(len(s)):
        p = len(s) - i - 1
        n = int(s[i]) * (10**p)

        if s[i] == '4' or s[i] == '9':
            # we need to get higher roman and subtract 1
            # but account the power (p)
            # if we are on last idx -> 10**0 = 1
            res.append(romans[vals.index(10**p)])
            res.append(romans[vals.index(n+10**p)])
        else:
            # convert to largest possible romans
            for j in range(len(vals)):
                if vals[j] <= n:
                    while n - vals[j] >= 0:
                        res.append(romans[j])
                        n -= vals[j]

    return "".join(res)

num = int(input())
print(intToRoman(num))
