n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'I':
            start_x, start_y = i, j

def dfs(sx, sy):
    stack = []
    visited[sx][sy] = 1
    vx, vy = sx, sy
    global cnt

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while True:
        for k in range(4):
            nx = vx + dx[k]
            ny = vy + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and matrix[nx][ny] != 'X':
                stack.append((vx, vy))
                visited[nx][ny] = 1
                if matrix[nx][ny] == 'P':
                    cnt += 1
                vx, vy = nx, ny
                break
        else:
            if stack:
                vx, vy = stack.pop()
            else:
                break

dfs(start_x, start_y)
if cnt == 0:
    print('TT')
else:
    print(cnt)