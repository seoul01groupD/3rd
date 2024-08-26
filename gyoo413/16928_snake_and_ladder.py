n, m = map(int, input().split())
lst = []
for _ in range(n + m):
    lst.extend(list(map(int, input().split())))
adjL = [[] for _ in range(101)]
for i in range(len(lst) // 2):
    v1, v2 = 