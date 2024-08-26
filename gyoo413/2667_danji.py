n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
danji = 0


def dfs(sx, sy):
    stack = []
    cnt = 1
    visited[sx][sy] = 1
    global danji

    while True:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                stack.append((sx, sy))
                visited[nx][ny] = 1
                sx = nx
                sy = ny
                cnt += 1
                break
        else:
            if stack:
                sx, sy = stack.pop()
            else:
                danji += 1
                return cnt
            
ans_lst = []
for x in range(n):
    for y in range(n):
        if visited[x][y] == 0 and matrix[x][y] == 1:
            result = dfs(x, y)
            ans_lst.append(result)
ans_lst.sort()
print(danji)
for ans in ans_lst:
    print(ans)