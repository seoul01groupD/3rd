N , M = map(int, input().split())

T = int(input())
temp = []
for tc in range(T):
    i, j = map(int, input().split())
    temp.append((i,j))


x , y = map(int, input().split())
min_value = 0
for i, j in temp:
    min_value2 = []
    left = 0
    right = 0
    if x == 1:
        if i == 1:
            min_value += abs(y-j)
        elif i == 3:
            min_value += y
            min_value += M - j - 1
        elif i == 4:
            min_value += N - y
            min_value += M - j - 1
        else:
            left += y + M + j
            right += N-y + M + N-j
            min_value2.append(left)
            min_value2.append(right)
            min_value += min(min_value2)


    elif x == 2:
        if i == 1:
            left += y + M + j
            right += N - y + M + N - j
            min_value2.append(left)
            min_value2.append(right)
            min_value += min(min_value2)
        elif i == 3:
            min_value += y
            min_value += j + 1
        elif i == 4:
            min_value += N - y
            min_value += j + 1
        else:
            min_value += abs(y - j)
    elif x == 3:
        if i == 1:
            min_value += M-y + 1
            min_value += j
        elif i == 3:
            min_value += abs(y - j)
        elif i == 4:
            left += M - y + 1 + N + M-j+1
            right += y+1 + N + j+1
            min_value2.append(left)
            min_value2.append(right)
            min_value += min(min_value2)

        else:
            min_value += y+1
            min_value += j
    elif x == 4:
        if i == 1:
            min_value += M - y + 1
            min_value += M - j
        elif i == 3:
            left += y+1 + N + j+1
            right += M - y-1 + N + M - j-1
            min_value2.append(left)
            min_value2.append(right)
            min_value += min(min_value2)

        elif i == 4:
            min_value += abs(y - j)

        else:
            min_value += y+1
            min_value += M - j

print(min_value)

