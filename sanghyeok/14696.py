N = int(input())

for tc in range(N):
    A1 = list(map(int, input().split()))
    B1 = list(map(int, input().split()))
    A = A1[1:]
    B = B1[1:]

    A_4 = 0
    B_4 = 0
    A_3 = 0
    B_3 = 0
    A_2 = 0
    B_2 = 0
    A_1 = 0
    B_1 = 0
    for i in A:
        if i == 1:
            A_1 +=1
        elif i == 2:
            A_2 +=1
        elif i == 3:
            A_3 +=1
        else:
            A_4 +=1
    for i in B:
        if i == 1:
            B_1 +=1
        elif i == 2:
            B_2 +=1
        elif i == 3:
            B_3 +=1
        else:
            B_4 +=1

    if A_4 > B_4:
        print('A')
    elif A_4 < B_4:
        print('B')
    else:
        if A_3 > B_3:
            print('A')
        elif A_3 < B_3:
            print('B')
        else:
            if A_2 > B_2:
                print('A')
            elif A_2 < B_2:
                print('B')
            else:
                if A_1 > B_1:
                    print('A')
                elif A_1 < B_1:
                    print('B')
                else:
                    print('D')