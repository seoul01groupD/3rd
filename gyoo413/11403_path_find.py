n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]
adjL = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if adj_matrix[i][j] == 1:
            adjL[i].append(j)

def dfs(start, end):
    visited = [0] * n
    stack = []
    v = start

    while True:
        for w in adjL[v]:
            if visited[w] == 0:
                stack.append(v)
                visited[w] = 1
                if w == end:
                    return 1
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return 0
            
ans_mat = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans_mat[i][j] = dfs(i, j)
    print(*ans_mat[i])