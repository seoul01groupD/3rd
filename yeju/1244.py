# 남학생의 스위치
def men(arr,N,idx):
    for i in range(1, N//idx+1):   # 인덱스 배수만큼
        idx_m = idx * i - 1
        if arr[idx_m] == 0:
            arr[idx_m] = 1
        elif arr[idx_m] == 1:
            arr[idx_m] = 0
    return arr

# 여학생의 스위치
def women(arr,N,idx):
    idx -= 1
    back = idx - 1
    next = idx + 1
    for i in range(N):
        if back >= 0 and next < N:   # 인덱스 범위 지정
            if arr[back] == arr[next]:   # 양옆에 같으면 스위치 변경
                if arr[back] == 0:
                    arr[back] = arr[next] = 1
                else:
                    arr[back] = arr[next] = 0
                back -= 1
                next += 1
            else:
                break
        else:
            break
    if arr[idx] == 0:
        arr[idx] = 1
    else:
        arr[idx] = 0
    return arr

import sys
inputs = sys.stdin.readline()
N = int(inputs)
arr = list(map(int,inputs.split()))
S = int(inputs)

# N = int(input())
# arr = list(map(int,input().split()))
# S = int(input())
for _ in range(S):
    s, s_idx = map(int,inputs.split())
    # 성별에 따라 스위치 조정
    if s == 1:
        arr = men(arr,N,s_idx)
    else:
        arr = women(arr,N,s_idx)

# 20개씩 출력하기
for i in range(0,N,20):
    print(*arr[i:i+20])