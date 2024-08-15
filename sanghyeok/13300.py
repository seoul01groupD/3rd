import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0]*2 for _ in range(6)]

for i in range(N):
    S, Y = map(int, input().split())
    arr[Y-1][S] += 1
room = 0
for i in arr:
    for i2 in i:
        if i2%K != 0:
            room += i2//K + 1
        else:
            room += i2//K

print(room)
