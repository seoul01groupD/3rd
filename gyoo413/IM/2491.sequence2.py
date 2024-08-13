n = int(input())
lst = list(map(int, input().split()))

cnt_list = [1]; cnt = 1
for i in range(1, n):
    if lst[i] <= lst[i - 1]:
        cnt += 1
    else:
        cnt_list.append(cnt)
        cnt = 1
    if i == n - 1:
        cnt_list.append(cnt)
cnt = 1
for i in range(1, n):
    if lst[i] >= lst[i - 1]:
        cnt += 1
    else:
        cnt_list.append(cnt)
        cnt = 1
    if i == n - 1:
        cnt_list.append(cnt)

print(max(cnt_list))