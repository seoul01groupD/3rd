import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    k = int(input())
    for _ in range(k):
        op, num = input().split()
        num = int(num)
        max_cnt = 0
        min_cnt = 0
        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            max_cnt += 1
            min_cnt += 1
        else:
            if num == 1:
                heapq.heappop(max_heap)
                max_cnt -= 1
                if max_cnt == 0:
                    min_heap = []
                    min_cnt = 0
            else:
                heapq.heappop(min_heap)
                min_cnt -= 1
                if min_cnt == 0:
                    max_heap = []
                    max_cnt = 0

    if (not min_heap) or (not max_heap) or (min_heap[0] > -max_heap[0]):
        print('EMPTY')
    else:
        print(-max_heap[0], min_heap[0])