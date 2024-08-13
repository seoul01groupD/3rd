import sys
input = sys.stdin.readline

matrix = [[0] * 1001 for _ in range(1001)]
n = int(input())

for k in range(1, n + 1):
    start_x, start_y, width, height = map(int, input().split())
    for i in range(start_x, start_x + width):
        for j in range(start_y, start_y + height):
            matrix[i][j] = k

for idx in range(1, n + 1):
    ans = 0
    for i in range(len(matrix)):
        ans += matrix[i].count(idx)
    print(ans)
