# import sys
# input = sys.stdin.readline

def bfs(row, col,N, arr,  visited):
    queue = [(row,col)]
    visited[row][col] = 1
    count = 0
    while queue:
        i, j = queue.pop(0)
        count +=1
        d_row = [1,0,-1,0]
        d_col = [0,1,0,-1]
        for k in range(4):
            n_row = i + d_row[k]
            n_col = j + d_col[k]
            if 0<= n_row<N and 0<= n_col<N and arr[n_row][n_col] == 1 and visited[n_row][n_col] == 0:
                visited[n_row][n_col] = 1
                queue.append((n_row,n_col))
    return count


N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]* N for _ in range(N)]
count_2 = 0
result = []

for row in range(N):
    for col in range(N):
        if arr[row][col] == 1 and visited[row][col] == 0:
            result.append(bfs(row,col,N, arr,visited))
            count_2+=1

result.sort()
print(count_2)
for i in result:
    print(i)
