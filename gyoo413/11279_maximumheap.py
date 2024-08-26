import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
heapq.heapify(arr)
for i in range(n):
    integer = int(input())
    if integer != 0:
        heapq.heappush(arr, -integer)
    else:
        if arr:
            result = -heapq.heappop(arr)
            print(result)
        else:
            print(0)