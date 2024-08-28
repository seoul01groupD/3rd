n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if matrix[x][y] == 2:
            sx, sy = x, y

queue = [(sx, sy)]
visited[sx][sy] = 1

while queue:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    tx, ty = queue.pop(0)
    for k in range(4):
        nx = tx + dx[k]
        ny = ty + dy[k]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and matrix[nx][ny] == 1:
            visited[nx][ny] = visited[tx][ty] + 1
            queue.append((nx, ny))

ans_lst = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visited[i][j] > 0:
            ans_lst[i][j] = visited[i][j] - 1
        if visited[i][j] == 0 and matrix[i][j] == 0:
            ans_lst[i][j] = 0
        elif visited[i][j] == 0 and matrix[i][j] == 1:
            ans_lst[i][j] = -1
    print(*ans_lst[i])