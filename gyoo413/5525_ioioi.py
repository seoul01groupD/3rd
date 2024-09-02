import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

cnt = 0
temp = 0
for i in range(1, m):
    if s[i] != s[i - 1]:
        temp += 1
        if temp == 2 * n:
            if s[i] == 'I':
                cnt += 1
                temp -= 2
            else:
                temp -= 1
    else:
        temp = 0

print(cnt)