import sys

input = sys.stdin.readline




arr = [[0]*100 for _ in range(100)]

N = int(input())

for i in range(N):
    L , D = map(int, input().split())
    for i2 in range(10):
        for i3 in range(10):
            if arr[i2+L][i3+D] == 0:
                arr[i2+L][i3+D] = 1



result = 0
for i in arr:
    result += sum(i)



print(result)








