import sys

input = sys.stdin.readline
arr = [[0]*100 for _ in range(100)]

T = 4

for tc in range(T):
    Lx,Ly,Rx,Ry = map(int, input().split())
    for i in range(Lx,Rx):
        for i2 in range(Ly,Ry):
            if arr[i][i2] == 0:
                arr[i][i2] = 1
    result_sum = 0
    for i in arr:
        result_sum += sum(i)


print(result_sum)

