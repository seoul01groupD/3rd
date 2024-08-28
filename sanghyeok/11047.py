N , K = map(int, input().split())
arr = []
b = 0
for tc in range(N):
    a = int(input())
    arr.append(a)

for i in arr[::-1]:
    if K ==0:
        break
    elif i>K:
        continue

    else:
        b += K//i
        K = K%i

print(b)