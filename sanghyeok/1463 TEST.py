N = int(input())

# DP 테이블 초기화
dp = [0] * (N + 1)

# DP 진행
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1  # 1을 빼는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
