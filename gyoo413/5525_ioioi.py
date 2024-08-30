import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

cnt = []
for i in range(1, n + 1):
    temp = 0
    if s[i] == 'O':
        if s[i] != s[i - 1]:
            temp += 1
