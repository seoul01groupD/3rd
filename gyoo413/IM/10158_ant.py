import sys
input = sys.stdin.readline

n, m = map(int, input().split())
w, h = map(int, input().split())
time = int(input())

big, small = max(2 * n, 2 * m), min(2 * n, 2 * m)

while big % small != 0:
    big, small = small, big % small

gcd = small
lcm = gcd * (2 * n // gcd) * (2 * m // gcd)

time %= lcm
w += time
h += time
while w > n or w < 0:
    if w > n:
        w = 2 * n - w
        if w < 0:
            w = -w
while h > m or h < 0:
    if h > m:
        h = 2 * m - h
        if h < 0:
            h = -h

print(w, h)