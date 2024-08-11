matrix = [list(map(int, input().split())) for _ in range(5)]
bingo = []
for i in range(5):
    bingo.extend(list(map(int, input().split())))

def check(n):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == n:
                return (i, j)
            
            
def check_bingo(mat):
    
    cnt_diag1 = 0
    cnt_diag2 = 0
    count = 0

    for i in range(5):
        if mat[i][i] == 1:
            cnt_diag1 += 1
        if mat[i][4 - i] == 1:
            cnt_diag2 += 1
        cnt_col = 0
        cnt_row = 0
        for j in range(5):
            if mat[i][j] == 1:
                cnt_row += 1
            if mat[j][i] == 1:
                cnt_col += 1
        
        if cnt_row == 5:
            count += 1
        if cnt_col == 5:
            count += 1

    if cnt_diag1 == 5:
        count += 1
    if cnt_diag2 == 5:
        count += 1

    return count


ans_matrix = [[0] * 5 for _ in range(5)]

for i in range(25):
    
    x, y = check(bingo[i])
    ans_matrix[x][y] = 1

    if check_bingo(ans_matrix) >= 3:
        print(i + 1)
        break