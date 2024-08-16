# 2116

# index 함수
def find_idx(arr,value):
    n = 0
    for x in arr:
        if x == value:
            return n
        else:
            n += 1
import copy
N = 5
dice = [[2,3,1,6,5,4],[3,1,2,4,6,5],[5,6,4,1,3,2],[1,3,6,2,4,5],[4,1,6,5,2,3]]
#  [list(map(int,input().split())) for _ in range(N)]


# lst_all =
sum_dice = 0

for i in range(6):
    lst = copy.deepcopy(dice)
    sum_row = []
    for j in range(5):
        if j == 0:
            if i == 0:
                a, b = lst[j][0], lst[j][5]
            elif i == 1 or i == 2:
                a, b = lst[j][i], lst[j][i+2]
            elif i == 3 or i == 4:
                a, b = lst[j][i], lst[j][i - 2]
            else:
                a, b = lst[j][5], lst[j][0]
            print(a,b)

        else:
            idx = find_idx(lst[j], b)
            if idx == 0:
                a, b = lst[j][0], lst[j][5]
            elif idx == 1 or idx == 2:
                a, b = lst[j][idx], lst[j][idx+2]
            elif idx == 3 or idx == 4:
                a, b = lst[j][idx], lst[j][idx - 2]
            else:
                a, b = lst[j][5], lst[j][0]
        if dice[j][i] != a and dice[j][i] != b:
            sum_row.append(dice[j][i])
            print(a,b)

        # print(sum_row)
