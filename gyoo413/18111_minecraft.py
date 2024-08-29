import sys
input = sys.stdin.readline

n, m, inven = map(int, input().split())
mine = []
for _ in range(n):
    mine.extend(list(map(int, input().split())))

def add(arr, idx):
    global temp_inven, time
    arr[idx] += 1
    temp_inven -= 1
    time += 1

def subtract(arr, idx):
    global temp_inven, time
    arr[idx] -= 1
    temp_inven += 1
    time += 2

ans_list = []
for height in range(257):
    if height * m * n > sum(mine) + inven:
            break
    temp = mine.copy()
    temp_inven = inven
    time = 0
    for j in range(n * m):
        if temp[j] == height:
            continue
        while temp[j] > height:
            subtract(temp, j)
        while temp[j] < height and temp_inven:
            add(temp, j)
        
    ans_list.append([time, temp[0]])

min_time = ans_list[0][0]
result = ans_list[0]
for ans in ans_list:
    if ans[0] < min_time:
        result = ans

print(*result)
