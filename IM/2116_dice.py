n = int(input())
dice = []


def change(idx):
    if idx == 1 or idx == 2:
        top = idx + 2
    elif idx == 3 or idx == 4:
        top = idx - 2
    elif idx == 0:
        top = 5
    else:
        top = 0
    return top


for i in range(n):
    dice.append(list(map(int, input().split())))

top_bottom = []

for i in range(6):
    top = change(i)
    lst = [(dice[0][i], dice[0][top])]

    for j in range(1, n):
        bottom = top

        for k in range(6):
            if dice[j][k] == dice[j - 1][top]:
                bottom = k

        top = change(bottom)
        lst.append((dice[j][bottom], dice[j][top]))

    top_bottom.append(lst)

total_list=[]

for i in range(6):
    total = 0
    for tup in top_bottom[i]:
        if 6 not in tup:
            total += 6
        if 6 in tup and 5 not in tup:
            total += 5
        elif 6 in tup and 5 in tup:
            total += 4

    total_list.append(total)

ans = max(total_list)
print(ans)