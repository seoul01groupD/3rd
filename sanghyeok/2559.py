import sys
input = sys.stdin.readline


N, K = map(int, input().split())

arr = list(map(int, input().split()))


a_sum = sum(arr[:K])
max_sum = a_sum

for i in range(1,N-K+1):
    a_sum = a_sum - arr[i-1] + arr[i+K-1]
    if a_sum > max_sum:
        max_sum = a_sum



print(max_sum)