

arr = [list(map(int,input().split())) for _ in range(5)]

mc_arr = [list(map(int, input().split())) for _ in range(5)]

arr_2 = [[1]*5 for _ in range(5)]
mc_arr2 = []
for i in mc_arr:
     for j in i:
         mc_arr2.append(j)

def bingo_row(arr):
    bingo = 0
    for row in range(5):
        if sum(arr[row]) == 0:
            bingo +=1
    return bingo

def bingo_col(arr):
    bingo = 0
    for col in range(5):
        if sum(arr[row][col] for row in range(5)) == 0:
            bingo +=1
    return bingo


def bingo_x(arr):
    bingo = 0
    if sum(arr[row][row] for row in range(5)) == 0:
        bingo +=1
    if sum(arr[row][4-row] for row in range(5)) == 0:
        bingo += 1
    return bingo





counts = 0
bingo = 0
for j in mc_arr2:
    for row in range(5):
        for col in range(5):
            if arr[row][col] == j:
                arr_2[row][col] = 0
    counts +=1


    bingo = bingo_row(arr_2) + bingo_col(arr_2) + bingo_x(arr_2)

    if bingo >=3:
        print(counts)
        break






