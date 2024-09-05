n = int(input())
counsel = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 6)
for cur in range(n):
    day, pay = counsel[cur]
    finish = cur + day
    cur_max = max(dp[:cur + 1])
    if dp[cur] < cur_max:
        dp[cur] = cur_max
    dp[finish] = max(cur_max + pay, dp[finish])
    
result = max(dp[:n + 1])

print(result)