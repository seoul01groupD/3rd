n, m = map(int, input().split())
count = int(input())
row = [0, m]
col = [0, n]
for i in range(count):
    direction, number = map(int, input().split())
    if direction == 0:
        row.append(number)
    else:
        col.append(number)

row.sort()
col.sort()
width = []
height = []
for i in range(len(row) - 1):
    width.append(row[i + 1] - row[i])
for i in range(len(col) - 1):
    height.append(col[i + 1] - col[i])

area = 0
for x in width:
    for y in height:
        if x * y > area:
            area = x * y

print(area)