# 2559
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
arr = list(map(int,input().split()))

# 슬라이드 인덱스
max_temp = []
max_temp.append(sum(arr[:K]))
for i in range(N-K):
    max_temp.append(max_temp[i] - arr[i] + arr[k+1])

print(max(max_temp))