
def exist(board, word) -> bool:
    N, M = len(board), len(board[0])
    def dfs(i, j, cur_idx):
        if cur_idx >= len(word):
            return True

        temp = board[i][j]
        board[i][j] = '1'

        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == word[cur_idx]:
                if dfs(ni, nj, cur_idx + 1):
                    return True

        board[i][j] = temp
        return False

    for i in range(N):
        for j in range(M):
            if board[i][j] == word[0] and dfs(i, j, 1):
                return True

    return False

N, M = map(int, input().split())
board = [[x for x in input().split()] for _ in range(N)]
word = input()
print(exist(board, word))
