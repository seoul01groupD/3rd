n, k = map(int, input().split())
temperature = list(map(int, input().split()))

ans = 0; temp = 0
for i in range(k):
    ans += temperature[i]
    temp += temperature[i]

for i in range(1, n - k + 1):
    temp -= temperature[i - 1]
    temp += temperature[i + k - 1]
    if temp > ans:
        ans = temp

print(ans)
        