import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
heapq.heapify(heap)

for _ in range(n):
    num = int(input())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))
    