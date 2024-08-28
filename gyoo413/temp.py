import sys
input = sys.stdin.readline

K,N = map(int,input().split())
arr = [int(input()) for _ in range(K)]
x = max(arr)

def binary(arr,start,end):
    middle = (start + end) // 2
    c = 0
    if middle >= end or start >= middle:
        return middle
    else:
        for i in range(K):
            c += arr[i] // middle
        if c < N:
            return binary(arr,start,middle)
        elif c >= N:
            return binary(arr,middle,end)

print(binary(arr,1,x))