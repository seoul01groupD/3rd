n = int(input())
counsel = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)
