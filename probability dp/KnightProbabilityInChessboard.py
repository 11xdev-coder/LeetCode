def knightProbability(n, k, row, column) -> float:
    dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]
    dp[0][row][column] = 1

    moves = [
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1)
    ]
    for step in range(1, k+1):
        for i in range(n):
            for j in range(n):
                for r, c in moves:
                    new_r = i + r
                    new_c = j + c
                    if 0 <= new_r < n and 0 <= new_c < n:
                        dp[step][i][j] += dp[step-1][new_r][new_c] / 8

    res = 0
    for i in range(n):
        for j in range(n):
            res += dp[k][i][j]

    return res

n, k, row, column = map(int, input().split())
print(knightProbability(n, k, row, column))
