import sys
input = sys.stdin.readline

v, e = map(int, input().split())
lst = []
for i in range(e):
    lst.extend(list(map(int, input().split())))
adjL = [[] for _ in range(v + 1)]
for i in range(e):
    v1, v2 = lst[2*i], lst[2*i + 1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)
visited = [0] * (v + 1)

def DFS(s, n):
    stack = []
    v = s
    visited[v] = 1
    
    while True:
        for w in adjL[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

cnt = 0
for i in range(1, v + 1):
    if visited[i] == 0:
        DFS(i, v)
        cnt += 1
    
print(cnt)