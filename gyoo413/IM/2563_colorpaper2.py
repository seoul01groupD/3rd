n = int(input())
matrix = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            matrix[x + i][y + j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        ans += matrix[i][j]

print(ans)