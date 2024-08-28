from collections import deque

N = int(input())
arr = deque(range(1, N + 1))

k = 0

while
    if len(arr) == 1:
        break
    elif k % 2 == 0:
        arr.popleft()
    else:
        arr.append(arr.popleft())
    k += 1

print(*arr)