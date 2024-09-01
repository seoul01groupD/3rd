def five_trees(x, y):

    dx = [-1, 0, 1, 1]
    dy = [1, 1, 1, 0]
    
    for k in range(4):
        cnt = 0
        nx = x + dx[k]
        ny = y + dy[k]
        while 0 <= nx < 19 and 0 <= ny < 19 and omokpan[x][y] == omokpan[nx][ny]:
            cnt += 1
            nx += dx[k]
            ny += dy[k]
        if cnt == 4 and 0 <= x - dx[k] and 0 <= y - dy[k] and omokpan[x - dx[k]][y - dy[k]] != omokpan[x][y]:
            return True
        elif cnt == 4 and (x - dx[k] < 0 or y - dy[k] < 0):
            return True

    return False

omokpan = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        flag = False
        if omokpan[i][j] == 1 and five_trees(i, j):
            print(1)
            print(i + 1, j + 1)
            flag = True
            break
        elif omokpan[i][j] == 2 and five_trees(i, j):
            print(2)
            print(i + 1, j + 1)
            flag = True
            break
    if flag:
        break
else:
    print(0)
