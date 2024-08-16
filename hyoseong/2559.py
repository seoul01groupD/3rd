# 수열

N, K = map(int, input().split())
day_lst = list(map(int, input().split()))

sum_temp = sum(day_lst[:K]) # 슬라이싱 윈도우
max_temp = sum_temp # 구간 합을 저장하고

for i in range(K, N):
    sum_temp += day_lst[i] - day_lst[i - K] # 양 끝값을 각각 더하고 빼기
    max_temp = max(max_temp, sum_temp)

print(max_temp)