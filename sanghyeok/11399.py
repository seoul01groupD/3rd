N = int(input())

arr = list(map(int, input().split()))

arr_min = sorted(arr)

# print(arr_min)
result = []
i = 0
while i < N:
    if result == []:
        result.append(arr_min[i])
    else:
        result.append(arr_min[i]+result[i-1])
    i +=1

sum_result = sum(result)
# print(result)
print(sum_result)