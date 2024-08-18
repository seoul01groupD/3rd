import sys

input = sys.stdin.readline


arr = [[0] * 1001 for _ in range(1001)]     # 

T = int(input())
counts = 1
temp = [0]*T


for tc in range(T):
    i, j, a, b = map(int,input().split())


    for row in range(i,i+a):
        for col in range(j,j+b):
            arr[row][col] = counts
    counts +=1


for count in range(T):
    temp[count] = 0
    for row in range(1001):
        for col in range(1001):
            if arr[row][col] == (count+1):
                temp[count] +=1
    print(temp[count])

