from collections import deque

def shortestPathBinaryMatrix(grid) -> int:
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
        
    N = len(grid)

    q = deque()
    q.append([0, 0])
    visited = [[False] * N for _ in range(N)]

    steps = 0
    while q:
        steps += 1
        
        for _ in range(len(q)):
            r, c = q.popleft()

            if r == (N-1) and c == (N-1):
                return steps

            for dr, dc in [[-1,0],[0, -1], [0, 1], [1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append([nr, nc])

    return -1
   
N = int(input())
grid = [[int(x) for x in input().split()] for _ in range(N)]
print(shortestPathBinaryMatrix(grid))