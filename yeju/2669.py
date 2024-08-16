import sys
input = sys.stdin.readline

arr = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(4):
    x_1,y_1,x_2,y_2 = map(int,input().split())
    for i in range(x_1,x_2):
        for j in range(y_1,y_2):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
print(cnt)