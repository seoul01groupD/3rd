n = int(input())
lst = list(map(int, input().split()))

line = [1]
for i in range(1, n):
    line.insert(i - lst[i], i + 1)

print(*line)
