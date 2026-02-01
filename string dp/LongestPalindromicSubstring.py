# substring is contigous!

def longestPalindromicSubstring(s: str) -> str:
    N = len(s)
    if N <= 1: # one letter
        return s
    
    # state: dp[i][j] -> is substring s[i:j] a palindrome
    dp = [[False] * N for _ in range(N)]
    start, end = 0, 0

    # len 1: every char is a palindrome
    for i in range(N):
        dp[i][i] = True

    # len 2: check if 2 chars are palindrome
    # because our relation is dp[i][j] = dp[i+1][j-1] and s[i] == s[j], having length 2 gives us:
    # 'babad' : dp[0][1] ('ba') = dp[1][0] ('ba'), which is incorrect
    for i in range(N-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start, end = i, i+1

    # now, check every length at every index
    for length in range(3, N+1): # include whole string
        for i in range(N - length + 1):
            j = i + length - 1
            
            # check if inner string is a palindrome, and 2 new characters at the end are equal
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                start, end = i, j

    return s[start:end+1] # in slicing last index is exclusive

print(longestPalindromicSubstring(input().strip()))

