n = int(input())
coordinate = list(map(int, input().split()))
sorted_coortdinate = sorted(coordinate)
count = {sorted_coortdinate[0]: 0}

for i in range(1, n):
    if sorted_coortdinate[i] == sorted_coortdinate[i - 1]:
        count.setdefault(sorted_coortdinate[i], count[sorted_coortdinate[i - 1]])
    else:
        count.setdefault(sorted_coortdinate[i], count[sorted_coortdinate[i - 1]] + 1)

for num in coordinate:
    print(count[num], end=' ')