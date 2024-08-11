n = int(input())
switch = list(map(int, input().split()))
m = int(input())


def change(number):
    idx = number - 1
    if switch[idx] == 0:
        switch[idx] = 1
    else:
        switch[idx] = 0


for i in range(m):
    gender, num = map(int, input().split())

    if gender == 1:
        for j in range(n):
            if (j + 1) % num == 0:
                change(j + 1)

    if gender == 2:
        change(num)
        j = 1
        while num - 1 - j >= 0 and num - 1 + j < n:
            if switch[num - 1 - j] == switch[num - 1 + j]:
                change(num + j)
                change(num - j)
                j += 1
            else:
                break

for i in range(len(switch)):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
