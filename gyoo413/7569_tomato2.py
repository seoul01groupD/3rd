from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [0, 0, 1, 0, 0, -1]
dy = [0, 1, 0, 0, -1, 0]
dz = [1, 0, 0, -1, 0, 0]

def bfs(sx, sy, sz):

    tx, ty, tz = sx, sy, sz

    for k in range(6):
        nx = tx + dx[k]
        ny = ty + dy[k]
        nz = tz + dz[k]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][nx][ny] == 0:
            tomato[nz][nx][ny] = tomato[tz][tx][ty] + 1
            tomato_lst.append((nx, ny, nz))


tomato_lst = deque()
for i in range(n):
    for j in range(m):
        for k in range(h):
            if tomato[k][i][j] == 1:
                tomato_lst.append((i, j, k))

while tomato_lst:
    x, y, z = tomato_lst.popleft()
    bfs(x, y, z)

min_day = 0
flag = False
for i in range(n):
    for j in range(m):
        for k in range(h):
            if tomato[k][i][j] > min_day:
                min_day = tomato[k][i][j]
            if tomato[k][i][j] == 0:
                min_day = 0
                flag = True
                break
        if flag:
            break
    if flag:
        break

print(min_day - 1)