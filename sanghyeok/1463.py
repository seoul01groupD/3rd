

import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
while True:

    if N == 1:
        break

    elif N >= 3:
        if N%3 == 0:
            N=N//3
            cnt+=1
        elif (N-1)%3 == 0:
            N = N-1
            N = N//3
            cnt += 2
        elif N%2 == 0:
            N = N//2
            cnt += 1
    else:
        N = N//2
        cnt += 1


print(cnt)

