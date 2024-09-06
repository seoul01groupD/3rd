import sys
input = sys.stdin.readline

n = int(input())
tanghuru = list(map(int, input().split()))

left = 0; right = 0
kind = {tanghuru[0]: 1}
max_count = 1
for right in range(1, n):
    if tanghuru[right] != tanghuru[right - 1]:
        if (tanghuru[right] not in kind) or kind[tanghuru[right]] == 0:
            kind[tanghuru[right]] = 1
            cnt = 0
            for v in kind.values():
                if v > 0:
                    cnt += 1
            while cnt > 2:
                kind[tanghuru[left]] -= 1
                if kind[tanghuru[left]] == 0:
                    cnt -= 1
                left += 1
        else:
            kind[tanghuru[right]] += 1
    else:
        kind[tanghuru[right]] += 1
                
    if max_count < (right - left + 1):
        max_count = right - left + 1

print(max_count)