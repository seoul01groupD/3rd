for _ in range(4):
    x1, y1, x2, y2, p1, q1, p2, q2 = map(int, input().split())
    if p1 < x1:
        x1, y1, x2, y2, p1, q1, p2, q2 = p1, q1, p2, q2, x1, y1, x2, y2

    if x2 > p1:
        if y1 <= q1:
            if y2 > q1:
                print('a')
            elif y2 == q1:
                print('b')
            else:
                print('d')
        else:
            if y1 > q2:
                print('d')
            elif y1 == q2:
                print('b')
            else:
                print('a')
    elif x2 == p1:
        if y1 <= q1:
            if y2 > q1:
                print('b')
            elif y2 == q1:
                print('c')
            else:
                print('d')
        else:
            if y1 > q2:
                print('d')
            elif y1 == q2:
                print('c')
            else:
                print('b')
    else:
        print('d')