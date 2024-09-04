import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]

d = [[-1, 1], [0, 1], [1, 1], [1, 0]]

result = []  # 이긴 사람 및 가장 왼쪽 바둑알의 좌표를 저장할 리스트
no_result = []

def black(arr):
    for i in range(19):
        for j in range(19):
            for k in range(4):
                cnt = 1
                flag = True
                ni = i + d[k][0]
                nj = j + d[k][1]
                while 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == 1:
                    cnt += 1
                    ni += d[k][0]
                    nj += d[k][1]
                    if cnt > 5:
                        flag = False
                        break
                if flag and cnt > 4 and arr[i - d[k][0]][j - d[k][0]] != 1:
                    r = [1, cnt, i + 1, j + 1]
                    result.append(r)

def white(arr):
    for i in range(19):
        for j in range(19):
            for k in range(4):
                cnt = 1
                flag = True
                ni = i + d[k][0]
                nj = j + d[k][1]
                while 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == 2:
                    cnt += 1
                    ni += d[k][0]
                    nj += d[k][1]
                    if cnt > 5:
                        flag = False
                        break
                if flag and cnt == 5 and arr[i - d[k][0]][j - d[k][0]] != 2:
                    r = [2, cnt, i + 1, j + 1]
                    result.append(r)

black(arr), white(arr)

print(result)

