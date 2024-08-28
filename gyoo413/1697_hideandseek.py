n, k = map(int, input().split())

queue = []
queue.append(n)
visit = [0] * 100001


def adj(n):
    return n - 1, n + 1, 2 * n


t = n
while queue:
    t = queue.pop(0)
    if t == k:
        print(visit[t])
        break
    for w in adj(t):
        if 0 <= w <= 100000 and visit[w] == 0:
            queue.append(w)
            visit[w] = visit[t] + 1