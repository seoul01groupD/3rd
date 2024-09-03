import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    for lst in start:
        vx, vy = lst[0], lst[1]
        queue.append((vx, vy))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        tx, ty = queue.popleft()
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]
            if 0 <= nx < n and 0 <= ny < m and (visited[nx][ny] == 0 or visited[nx][ny] > (visited[tx][ty] + 1)) and tomato[nx][ny] == 0:
                visited[nx][ny] = visited[tx][ty] + 1
                queue.append((nx, ny))


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

start = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            start.append([i, j])

bfs(start)

max_value = 0
flag = False
for i in range(n):
    for j in range(m):
        if visited[i][j] > max_value:
            max_value = visited[i][j]
        if visited[i][j] == 0 and tomato[i][j] == 0:
            flag = True
            max_value = -1
            break
    if flag:
        break

print(max_value)