import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    pop_dict = {}
    cnt = 0
    k = int(input())
    for _ in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':
            if pop_dict.get(num, False):
                pop_dict[num] += 1
            else:
                pop_dict[num] = 1
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
            cnt += 1
        else:
            if cnt > 0:
                if num == 1:
                    while max_heap and pop_dict[-max_heap[0]] < 1:
                        heapq.heappop(max_heap)
                    pop_dict[-max_heap[0]] -= 1
                else:
                    while min_heap and pop_dict[min_heap[0]] < 1:
                        heapq.heappop(min_heap)
                    pop_dict[min_heap[0]] -= 1
                cnt -= 1
        # print('max_heap: ', max_heap)
        # print('min_heap: ', min_heap)
        # print('pop_dict: ', pop_dict)

    if cnt > 0:
        while max_heap and pop_dict[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        while min_heap and pop_dict[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        print(-max_heap[0], min_heap[0])
    else:
        print('EMPTY')

    