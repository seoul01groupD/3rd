v, e = map(int, input().split())
adjL = [[] for _ in range(v + 1)]
for _ in range(e):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)


def bfs(s, end):
    
    visited = [0] * (v + 1)

    if s == end:
        return 0
    
    queue = []
    visited[s] = 1
    queue.append(s)

    while queue:
        t = queue.pop(0)
        for w in adjL[t]:
            if visited[w] == 0:
                visited[w] = visited[t] + 1
                queue.append(w)
    
    return visited[end] - 1

minimum = v * (v - 1)
bacon = 0
for i in range(1, v + 1):
    total = 0
    for j in range(1, v + 1):
        total += bfs(i, j)
    if total < minimum:
        minimum = total
        bacon = i

print(bacon)
