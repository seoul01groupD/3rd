import sys


N = int(input())




def A(a,b):
    temp = [a,b]
    while True:
        next = temp[-2] - temp[-1]
        if next< 0:
            break
        temp.append(next)

    return temp


def B(a):
    max_len = 0
    result = []

    for i in range(1, a+1):
        lst = A(a,i)
        if len(lst) > max_len:
            max_len = len(lst)
            result = lst

    return max_len, result

max_len, result = B(N)

print(max_len)
print(*result)






