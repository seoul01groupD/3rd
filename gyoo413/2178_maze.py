n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
queue = []
visited[0][0] = 1
queue.append((0, 0))

while queue:
    tx, ty = queue.pop(0)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for k in range(4):
        nx = tx + dx[k]
        ny = ty + dy[k]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maze[nx][ny] == 1:
            queue.append((nx, ny))
            visited[nx][ny] = visited[tx][ty] + 1
            if nx == n - 1 and ny == m - 1:
                print(visited[nx][ny])
                break