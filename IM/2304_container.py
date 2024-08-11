n = int(input())
column = []
for i in range(n):
    column.append(list(map(int, input().split())))
column.sort()

M = column[0][1]
for col in column:
    if col[1] > M:
        M = col[1]

stack = []

i = 0
while column[i][1] <= M:
    if (stack and column[i][1] >= stack[-1][1]) or not stack:
        stack.append(column[i])
    if  column[i][1] == M:
        break
    i += 1
M_idx = i

i += 1
while i < len(column):
    while column[i][1] > stack[-1][1]:
        stack.pop()
    stack.append(column[i])
    i += 1

area = 0
for j in range(len(stack) - 1):
    area += abs(stack[j + 1][0] - stack[j][0]) * min(stack[j][1], stack[j + 1][1])

area += M
print(area)