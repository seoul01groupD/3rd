import sys
input = sys.stdin.readline

n, m, inven = map(int, input().split())
mine = []
for _ in range(n):
    mine.extend(list(map(int, input().split())))
mine.sort(reverse=True)

def add(idx, target):
    global temp_inven, time
    move = target - idx
    idx += move
    temp_inven -= move
    time += move

def remove(idx, height):
    global temp_inven, time
    move = idx - height
    idx -= move
    temp_inven += move
    time += (2 * move)

min_height = min(mine)
max_height = max(mine)

ans_list = []
for height in range(min_height, max_height + 1):
    if height * m * n > sum(mine) + inven:
            break

    temp_inven = inven
    time = 0
    flag = True
    for block in mine:
        if block > height:
            remove(block, height)
        elif block < height:
            if temp_inven < 1:
                flag = False
                break
            add(block, height)

    if flag:
        ans_list.append([time, height])


min_time = ans_list[0][0]
result = ans_list[0]
for ans in ans_list:
    if ans[0] <= min_time:
        result = ans
        min_time = ans[0]

print(*result)


