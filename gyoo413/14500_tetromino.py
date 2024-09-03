n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

def tetromino1(sx, sy):
    result = 0
    if 0 <= sx < n - 1 and 0 <= sy < m - 1:
        result = sum(mat[sx][sy], mat[sx][sy + 1], mat[sx + 1][sy], mat[sx + 1][sy + 1])
    
    return result

def tetromino2(sx, sy):
    result1 = 0; result2 = 0
    if 0 <= sx < n and 0 <= sy < m - 3:
        for k in range(4):
            result1 += mat[sx][sy + k]
    elif 0 <= sx < n - 3 and 0 <= sy < m:
        for k in range(4):
            result2 += mat[sx + k][sy]
    
    return max(result1, result2)

def tetromino3(sx, sy):
    