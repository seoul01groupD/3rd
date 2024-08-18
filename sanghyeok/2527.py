T = 4

def a(arr):
    arr_count = 0
    for i in arr:
        arr_count += arr.count(i)

    return arr_count

for tc in range(T):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    score2 = x1, y1, p1, q1, x2, y2, p2, q2
    score = max(x1, y1, p1, q1, x2, y2, p2, q2)
    arr = [[0]*(score) for _ in range(score)]
    for row in range(x1,p1):
        for col in range(y1,q1):
            arr[row][col] += 1
    for row in range(x2,p2):
        for col in range(y2,q2):
            arr[row][col] += 1
    counts = 0
    counts2 = 0
    d_row = [-1,1,1,-1]
    d_col = [1,1,-1,-1]
    for row in range(score):
        for col in range(score):
            if arr[row][col] == 2:
                counts +=1
    # for k in range(4):
    #     n_row = d_row[k]
    if counts == 0:
        print('d')
    elif counts == 2:
        if a(score2) - len(score2) == 2:
            print('b')
    elif counts > 2:
            print('a')
    elif counts == 1:
        print('c')

