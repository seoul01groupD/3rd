n, m = map(int, input().split())
lst = []
for _ in range(n + m):
    lst.extend(list(map(int, input().split())))

adjL = [[] for _ in range(101)]
for i in range(n + m):
    v1, v2 = lst[i * 2], lst[i * 2 + 1]
    adjL[v1].append(v2)

visited = [0] * 101

queue = []
start = 1
queue.append(start)
visited[start] = 0

while queue:
    t = queue.pop(0)
    for dice in range(1, 7):
        n = t + dice
        if n < 101 and visited[n] == 0:
            visited[n] = visited[t] + 1

            if adjL[n] != []:
                n = adjL[n][0] 
                if visited[n] == 0:  
                    visited[n] = visited[t] + 1

            queue.append(n)

print(visited[100])

