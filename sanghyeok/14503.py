N , M = map(int, input().split())

#0이면 북, 1이면 동, 2이면 남, 3이면 서
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
d_row = [-1,0,1,0]
d_col = [0,1,0,-1]
cnt = 0
see = d

while True:
    if arr[r][c] == 0:
        arr[r][c] =2
        cnt +=1

    for i in range(4):
        see = (see + 3) % 4
        if arr[r+d_row[see]][c+d_col[see]] == 0:
            r = r + d_row[see]
            c = c + d_col[see]
            break


    else:
        reverse_d = (see + 2) % 4
        if arr[r + d_row[reverse_d]][c + d_col[reverse_d]] == 1:
            break
        r = r + d_row[reverse_d]
        c = c + d_col[reverse_d]







print(cnt)
