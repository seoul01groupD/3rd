n, m, inven = map(int, input().split())
mine = []
for _ in range(n):
    mine.extend(list(map(int, input().split())))
mine.sort()

time = 0
for i in range(n * m):
    