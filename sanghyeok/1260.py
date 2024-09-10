
def DFS(s,N):
    visited = [0] * (N+1)
    stack = []
    print(s, end=' ')
    visited[s] = 1
    v = s
    while True:
        for w in sorted(adjL[v]):
            if visited[w] == 0:
                stack.append(v)
                v = w
                print(v, end=' ')
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break




def BFS(s,N):
    visited = [0] * (N+1)
    q = [s]
    visited[s] =1
    while q:
        v= q.pop(0)
        print(v,end=' ')
        for w in sorted(adjL[v]):
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1



N,M,V = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

# print(arr)
# print(arr2)
adjL = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2 = arr[i]
    adjL[v1].append(v2)
    adjL[v2].append(v1)

DFS(V,N)
print()
BFS(V,N)

