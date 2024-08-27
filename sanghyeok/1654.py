import sys

def binary(arr):
    global start, end

    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for i in arr:
            cnt += i // mid

        if cnt < N:
            end = mid - 1

        else:
            start = mid + 1


    return end








input = sys.stdin.readline
K, N   = map(int,input().split())

arr =[]
for tc in range(K):
    n= int(input())
    arr.append(n)

start = 1
end = max(arr)

result= binary(arr)
print(result)






