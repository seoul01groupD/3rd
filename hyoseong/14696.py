# 딱지놀이

N = int(input())

for _ in range(N):
    paint_a = list(map(int, input().split()))
    paint_b = list(map(int, input().split()))
    win = 'D'

    for i in range(4, 0, -1): # 4부터 1까지 개수를 비교하여 승패를 판별
        if paint_a[1:].count(i) > paint_b[1:].count(i):
            win = 'A'
            break

        elif paint_a[1:].count(i) < paint_b[1:].count(i):
            win = 'B'
            break

    print(win)