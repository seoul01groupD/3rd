import sys
input = sys.stdin.readline

N = int(input())
arr= list(range(2, N+1, 2))
n = N % 2
k = len(arr) % 2

while True:
    if len(arr) == 1:
        break
    elif k == 0:
        arr.pop(0)

    elif k == 1:
        queue = arr.pop(0)
        arr.append(queue)
    k+=1

print(*arr)

# 1 2 3 4 5 6
# 2 3 4 5 6
# 3 4 5 6 2
# 4 5 6 2
# 5 6 2 4
# 6 2 4
# 2 4 6
# 4 6
# 6 4
# 4
# 1 2 3 4 5 6 7
# 2 3 4 5 6 7
# 3 4 5 6 7 2
# 4 5 6 7 2
# 5 6 7 2 4
# 6 7 2 4
# 7 2 4 6
# 2 4 6
# 4 6 2
# 6 2
# 2 6
# 6
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5 2
# 4 5 2
# 5 2 4
# 2 4
# 4 2
# 2
# 1 2 3 4 5 6 7 8
# 2 3 4 5 6 7 8
# 3 4 5 6 7 8 2
# 4 5 6 7 8 2
# 5 6 7 8 2 4
# 6 7 8 2 4
# 7 8 2 4 6
# 8 2 4 6
# 2 4 6 8
# 4 6 8
# 6 8 4
# 8 4
# 4 8
# 8
# 1 2 3 4 5 6 7 8 9 10
# 2 3 4 5 6 7 8 9 10
# 3 4 5 6 7 8 9 10 2
# 4 5 6 7 8 9 10 2
# 5 6 7 8 9 10 2 4
# 6 7 8 9 10 2 4
# 7 8 9 10 2 4 6
# 8 9 10 2 4 6
# 9 10 2 4 6 8
# 10 2 4 6 8
# 2 4 6 8 10
# 4 6 8 10
# 6 8 10 4
# 8 10 4
# 10 4 8
# 4 8
# 8 4
# 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 2
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 2
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 2 4
6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 2 4
7 8 9 10 11 12 13 14 15 16 17 18 19 20 2 4 6
8 9 10 11 12 13 14 15 16 17 18 19 20 2 4 6
9 10 11 12 13 14 15 16 17 18 19 20 2 4 6 8
10 11 12 13 14 15 16 17 18 19 20 2 4 6 8
11 12 13 14 15 16 17 18 19 20 2 4 6 8 10
12 13 14 15 16 17 18 19 20 2 4 6 8 10
13 14 15 16 17 18 19 20 2 4 6 8 10 12
14 15 16 17 18 19 20 2 4 6 8 10 12
15 16 17 18 19 20 2 4 6 8 10 12 14
16 17 18 19 20 2 4 6 8 10 12 14
17 18 19 20 2 4 6 8 10 12 14 16
18 19 20 2 4 6 8 10 12 14 16
19 20 2 4 6 8 10 12 14 16 18
20 2 4 6 8 10 12 14 16 18
2 4 6 8 10 12 14 16 18 20
4 6 8 10 12 14 16 18 20
6 8 10 12 14 16 18 20 4
8 10 12 14 16 18 20 4
10 12 14 16 18 20 4 8
12 14 16 18 20 4 8
14 16 18 20 4 8 12
16 18 20 4 8 12
18 20 4 8 12 16
20 4 8 12 16
4 8 12 16 20
8 12 16 20
12 16 20 8
16 20 8
20 8 16
8 16
16 8
8
