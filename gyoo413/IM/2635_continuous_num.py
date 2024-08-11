n = int(input())
length = 0
ans = []

for i in range(1, n + 1):
    lst = [n]
    lst.append(i)
    j = 2
    while True:
        if lst[j - 2] - lst[j - 1] < 0:
            break
        else:
            lst.append(lst[j - 2] - lst[j - 1])
            j += 1
    if len(lst) > length:
        length = len(lst)
        ans = lst

print(length)
print(*ans)