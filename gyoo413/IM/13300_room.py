n, k = map(int, input().split())
room = [[0] * 2 for _ in range(6)]
for _ in range(n):
    s, grade = map(int, input().split())
    room[grade - 1][s] += 1

cnt = 0
for i in range(6):
    for j in range(2):
        cnt += ((room[i][j] - 1) // k) + 1

print(cnt)