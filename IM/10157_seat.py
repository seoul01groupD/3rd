n, m = map(int, input().split())
K = int(input())

seat = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]

i = m; j = 0
num = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while num < n * m:

    for k in range(4):
        i += dx[k]
        j += dy[k]
        while 0 <= i < m and 0 <= j < n and visited[i][j] == 0:
            seat[i][j] = num
            visited[i][j] = 1

            i += dx[k]
            j += dy[k]
            num += 1

        i -= dx[k]
        j -= dy[k]

cnt = 0
for i in range(m):
    for j in range(n):
        if seat[i][j] == K:
            print(j + 1, m - i)
            break
        else:
            cnt += 1
if cnt == n * m:
    print(0)