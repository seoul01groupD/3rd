from collections import deque
import sys
input = sys.stdin.readline

def D(n):
    return (2 * n) % 10000

def S(n):
    if n > 0:
        return n - 1
    else:
        return 9999

def L(n):
    d1, d2, d3, d4 = n // 1000, (n // 100) % 10, (n // 10) % 10, n % 10
    return d2 * 1000 + d3 * 100 + d4 * 10 + d1

def R(n):
    d1, d2, d3, d4 = n // 1000, (n // 100) % 10, (n // 10) % 10, n % 10
    return d4 * 1000 + d1 * 100 + d2 * 10 + d3

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    visited = [0] * 10000

    visited[a] = ''
    queue = deque()
    queue.append((a, ''))

    while queue:
        flag = False
        t = queue.popleft()
        temp = [(D(t[0]), 'D'), (S(t[0]), 'S'), (L(t[0]), 'L'), (R(t[0]), 'R')]
        for k in range(4):
            if visited[temp[k][0]] == 0:
                visited[temp[k][0]] = visited[t[0]] + temp[k][1]
                queue.append(temp[k])
            if temp[k][0] == b:
                flag = True
                break
        if flag:
            break

    print(visited[b])