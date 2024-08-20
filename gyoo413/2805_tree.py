import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

start = 0; end = tree[-1]
while True:
    mid = (start + end) // 2
    height = mid
    get = 0
    for i in range(n):
        if tree[i] >= height:
            get += (tree[i] - height)
    
    if end - start <= 1:
        print(height)
        break

    if get == m:
        print(height)
        break

    elif get > m:
        start = mid

    else:
        end = mid