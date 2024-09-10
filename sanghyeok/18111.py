N,M,B = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arr_set = set()
# 제거해서 인벤토리 2초, 인벤토리에서 꺼내서 블록 쌓기 1초

for i in arr:
    for j in i:
        arr_set.add(j)

max_v = max(arr_set)
min_v = min(arr_set)
gap = []
for i in arr:
    for j in i:
        a = j- max_v
        gap.append(a)


# print(sum(gap))
result = []
if B >= abs(sum(gap)):
    result.append(abs(sum(gap)))
    result.append(max_v)
    result.append((N * M + sum(gap)) * 2)
    result.append(min_v)
else:
    result.append((N*M + sum(gap))*2)
    result.append(min_v)

# print(result)
if len(result) == 2:
    print(result[0], end=' ')
    print(result[1])
else:
    if result[0] < result[2]:
        print(result[0],end=' ')
        print(result[1])
    elif result[0] > result[2]:
        print(result[2], end= ' ')
        print(result[3])
    elif result[0] == result[2]:
        if result[1] > result[3]:
            print(result[0], end=' ')
            print(result[1])
        elif result[1] < result[3]:
            print(result[2], end=' ')
            print(result[3])
