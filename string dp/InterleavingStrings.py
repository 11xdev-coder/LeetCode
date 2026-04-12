def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    # dp[i][j] - can s1[0..i] and s2[0..j] be used to create s3[0..i+j]
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # 9 characters from s1 and 0 chars from s2 always can form 0 chars from s3
    dp[0][0] = True
    # fill first column -> if we take 0 chars from s3 then s1 must match s3 directly
    for i in range(1, len(s1)+1):
        if s1[i-1] == s3[i-1] and dp[i-1][0]:
            dp[i][0] = True

    # fill first row, same idea
    for j in range(1, len(s2)+1):
        if s2[j-1] == s3[j-1] and dp[0][j-1]:
            dp[0][j] = True

    # for character at s3[i+j-1] we have a choice:
    # take char from s1, then it must match and state before using this char must be  true
    # take char from s2 with same idea
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if (s1[i-1] == s3[i + j - 1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1]):
                dp[i][j] = True

    return dp[len(s1)][len(s2)]

s1 = input()
s2 = input()
s3 = input()
print(isInterleave(s1, s2, s3))
