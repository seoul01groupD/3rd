import sys
import copy
input = sys.stdin.readline

n = int(input())
color = [list(input().strip()) for _ in range(n)]
color2 = copy.deepcopy(color)
for i in range(n):
    for j in range(n):
        if color[i][j] == 'G' or color[i][j] == 'R':
            color2[i][j] = 'Z'
        else:
            color2[i][j] = color[i][j]
visited = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def normal_dfs(sx, sy):
    global cnt

    stack = []
    vx, vy = sx, sy
    visited[vx][vy] = 1

    while True:
        for k in range(4):
            nx = vx + dx[k]
            ny = vy + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and color[nx][ny] == color[sx][sy]:
                visited[nx][ny] = 1
                stack.append((vx, vy))
                vx, vy = nx, ny
                break
        else:
            if stack:
                vx, vy = stack.pop()
            else:
                cnt += 1
                break

def green_red_dfs(sx, sy):
    global cnt2

    stack = []
    vx, vy = sx, sy
    visited2[vx][vy] = 1

    while True:
        for k in range(4):
            nx = vx + dx[k]
            ny = vy + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited2[nx][ny] == 0 and color2[nx][ny] == color2[sx][sy]:
                visited2[nx][ny] = 1
                stack.append((vx, vy))
                vx, vy = nx, ny
                break
        else:
            if stack:
                vx, vy = stack.pop()
            else:
                cnt2 += 1
                break

cnt = 0; cnt2 = 0
for x in range(n):
    for y in range(n):
        if visited[x][y] == 0:
            normal_dfs(x, y)
        if visited2[x][y] == 0:
            green_red_dfs(x, y)

print(cnt, cnt2)
