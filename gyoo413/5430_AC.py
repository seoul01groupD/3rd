import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    func = input().strip()
    n = int(input())
    int_arr = input().strip().lstrip('[').rstrip(']').replace(',', ' ')
    int_arr = deque(map(int, int_arr.split()))
    cnt = 0
    for op in range(len(func)):
        flag = True
        if func[op] == 'R':
            cnt += 1
        else:
            if int_arr:
                if cnt % 2 == 0:
                    int_arr.popleft()
                else:
                    int_arr.pop()
            else:
                print('error')
                flag = False
                break
    if flag:
        str_arr = list(map(str, int_arr))
        if cnt % 2 != 0:
            str_arr = str_arr[::-1]
        ans = ','.join(str_arr)
        print('[', end='')
        print(ans, end='')
        print(']')