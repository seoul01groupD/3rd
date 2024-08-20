t = int(input())


def DFS(si, sj):
    stack = []
    v = [si, sj]
    visited[v[0]][v[1]] = 1
    global cnt

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while True:
        for k in range(4):
            t = [0, 0]
            t[0] = v[0] + dx[k]
            t[1] = v[1] + dy[k]
            if 0 <= t[0] < n and 0 <= t[1] < m and visited[t[0]][t[1]] == 0 and matrix[t[0]][t[1]] == 1:
                stack.append(v)
                visited[t[0]][t[1]] = 1
                v = t
                break
        else:
            if stack:
                v = stack.pop()
            else:
                cnt += 1
                break


for tc in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().split())
        matrix[j][i] = 1
    visited = [[0] * m for _ in range(n)]
    cnt = 0

    for x in range(n):
        for y in range(m):
            if visited[x][y] == 0 and matrix[x][y] == 1:
                DFS(x, y)

    print(cnt)