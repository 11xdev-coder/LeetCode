from collections import deque

def numIslands(grid) -> int:
    ans = 0

    def bfs(start_r, start_c, ans):
        q = deque()
        q.append([start_r, start_c])
        visited[start_r][start_c] = True

        while q:
            r, c = q.popleft()

            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and grid[nr][nc] == '1':
                    visited[nr][nc] = True
                    q.append([nr, nc])

    N, M = len(grid), len(grid[0])
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if grid[i][j] == '1' and not visited[i][j]:
                ans += 1
                # at each cell try to expand as far as possible
                bfs(i, j, ans)


    return ans
   
N = int(input())
grid = [[x for x in input().split()] for _ in range(N)]
print(numIslands(grid))