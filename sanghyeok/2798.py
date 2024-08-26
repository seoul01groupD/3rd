from itertools import combinations



N, M = map(int, input().split())

arr = list(map(int, input().split()))


arr2 = list(combinations(arr,3))
max_value = 0
for a,b,c in arr2:
    if sum((a,b,c)) == M:
        max_value = sum((a,b,c))
        break
    elif sum((a,b,c)) > M:
        continue
    elif sum((a,b,c)) < M and max_value<sum((a,b,c)):
        max_value = sum((a,b,c))

print(max_value)
