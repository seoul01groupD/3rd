T = int(input())

def before_max(temp):
    global score
    while True:
        if temp[0][1] == max_b:
            score += temp[0][1]
            break
        elif temp[0][1] < temp[1][1]:
            score += (temp[1][0] - temp[0][0]) * temp[0][1]
            temp.pop(0)

        else:
            temp.pop(1)

def after_max(temp):
    global score
    while True:
        if len(temp) == 1:
            break
        if len(temp) == 2:
            score += (temp[1][0] - temp[0][0]) * temp[1][1]
            break

        elif temp[1][1] <= temp[2][1]:
            temp.pop(1)
        else:
            score += (temp[1][0] - temp[0][0]) * temp[1][1]
            temp.pop(0)
            return after_max(temp)


temp = []
for tc in range(T):
    a , b = map(int, input().split())
    temp.append([a,b])

max_b = 0
temp.sort()
for a, b in temp:
    if max_b < b:
        max_b = b


score = 0
before_max(temp)
after_max(temp)
print(score)