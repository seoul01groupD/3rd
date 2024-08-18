C , R = map(int, input().split())
K = int(input())


if C * R < K:
    print(0)

else:
    arr = [[0]*C for _ in range(R)]
    d_row = [-1,0,1,0]
    d_col = [0,1,0,-1]
    k = 0
    num = 1
    row = R-1
    col = 0



    while num < K:

        arr[row][col] = num
        n_row = row + d_row[k]
        n_col = col + d_col[k]
        if n_row >= R or n_row < 0 or n_col >= C or n_col < 0 or arr[n_row][n_col] != 0:
            k = (k + 1) % 4
        row = row + d_row[k]
        col = col + d_col[k]
        num += 1



    print(f'{col + 1} {R-row}')




