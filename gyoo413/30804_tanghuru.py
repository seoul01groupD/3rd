from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tanghuru = deque(map(int, input().split()))
length = len(set(tanghuru))
start = 0; end = n - 1

while True:
    if length <= 2:
        break

    temp_start = tanghuru.popleft()
    temp_length = len(set(tanghuru))
    if length == temp_length:
        tanghuru.appendleft(temp_start)
        start += 1
    else:
        length = temp_length
        if length <= 2:
            break

    temp_end = tanghuru.pop()
    temp_length = len(set(tanghuru))
    if length == temp_length:
        tanghuru.append(temp_end)
        end -= 1
    else:
        length = temp_length

print(len(tanghuru))
    