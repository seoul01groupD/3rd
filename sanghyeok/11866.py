N , K = map(int, input().split())

arr = []
arr2 = []
for i in range(1,N+1):
    arr.append(i)

q = K-1
while True:
    if len(arr) == 1:
        arr2.append(arr[0])
        break
    queue = arr.pop(q)
    arr2.append(queue)
    q = (q + K-1)%len(arr)

result = "<" + ", ".join(map(str, arr2)) + ">"
print(result)
