import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

cnt = 0
for i in range(m - 1):
    temp_cnt = 0
    if s[i] == 'I':
        for j in range(i, i + 2 * n):
            if j < m - 1 and s[j] != s[j + 1]:
                temp_cnt += 1
            else:
                break
        if temp_cnt == 2 * n:
            cnt += 1

print(cnt)