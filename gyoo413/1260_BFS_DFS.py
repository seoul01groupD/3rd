def DFS(s, n):
    visited = [0] * (n + 1)
    stack = []
    v = s
    visited[v] = 1
    print(v, end=' ')

    while True:
        for w in adjL[v]:
            if visited[w] == 0:
                stack.append(v)
                visited[w] = 1
                print(w, end=' ')
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

def BFS(s, n):
    visited = [0] * (n + 1)
    queue = []
    v = s
    visited[v] = 1
    queue.append(v)

    while queue:
        t = queue.pop(0)
        print(t, end=' ')
        for w in adjL[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1


n, m, v = map(int, input().split())
lst = []
for _ in range(m):
    lst.extend(list(map(int, input().split())))

adjL = [[] for _ in range(n + 1)]
for i in range(m):
    v1, v2 = lst[2 * i], lst[2 * i + 1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)
for i in range(1, n + 1):
    adjL[i].sort()

DFS(v, n)
print()
BFS(v, n)

                