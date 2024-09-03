def tetromino1(sx, sy):
    result = 0
    if 0 <= sx < n - 1 and 0 <= sy < m - 1:
        result = mat[sx][sy] + mat[sx][sy + 1] + mat[sx + 1][sy] + mat[sx + 1][sy + 1]
    return result

def tetromino2(sx, sy):
    result1 = 0; result2 = 0
    if 0 <= sx < n and 0 <= sy < m - 3:
        for k in range(4):
            result1 += mat[sx][sy + k]
    if 0 <= sx < n - 3 and 0 <= sy < m:
        for k in range(4):
            result2 += mat[sx + k][sy]
    
    return max(result1, result2)

def tetromino3(sx, sy):
    result1 = 0; result2 = 0; result3 = 0; result4 = 0
    result5 = 0; result6 = 0; result7 = 0; result8 = 0
    if 2 <= sx < n and 0 <= sy < m - 1:
        for k in range(3):
            result1 += mat[sx - k][sy]
        result1 += mat[sx][sy + 1]
    if 2 <= sx < n and 1 <= sy < m:
        for k in range(3):
            result2 += mat[sx - k][sy]
        result2 += mat[sx][sy - 1]
    if 0 <= sx < n - 2 and 0 <= sy < m - 1:
        for k in range(3):
            result3 += mat[sx + k][sy]
        result3 += mat[sx][sy + 1]
    if 0 <= sx < n - 2 and 1 <= sy < m:
        for k in range(3):
            result4 += mat[sx + k][sy]
        result4 += mat[sx][sy - 1]
    if 1 <= sx < n and 2 <= sy < m:
        for k in range(3):
            result5 += mat[sx][sy - k]
        result5 += mat[sx - 1][sy]
    if 1 <= sx < n and 0 <= sy < m - 2:
        for k in range(3):
            result6 += mat[sx][sy + k]
        result6 += mat[sx - 1][sy]
    if 0 <= sx < n - 1 and 2 <= sy < m:
        for k in range(3):
            result7 += mat[sx][sy - k]
        result7 += mat[sx + 1][sy]
    if 0 <= sx < n - 1 and 0 <= sy < m - 2:
        for k in range(3):
            result8 += mat[sx][sy + k]
        result8 += mat[sx + 1][sy]
    return max(result1, result2, result3, result4, result5, result6, result7, result8)

def tetromino4(sx, sy):
    result1 = 0; result2 = 0; result3 = 0; result4 = 0
    if 1 <= sx < n - 1 and 0 <= sy < m - 1:
        result1 = mat[sx - 1][sy] + mat[sx][sy] + mat[sx][sy + 1] + mat[sx + 1][sy + 1]
    if 1 <= sx < n - 1 and 1 <= sy < m:
        result2 = mat[sx - 1][sy] + mat[sx][sy] + mat[sx][sy - 1] + mat[sx + 1][sy - 1]
    if 1 <= sx < n and 1 <= sy < m - 1:
        result3 = mat[sx][sy - 1] + mat[sx][sy] + mat[sx - 1][sy] + mat[sx - 1][sy + 1]
    if 1 <= sx < n and 1 <= sy < m - 1:
        result4 = mat[sx - 1][sy - 1] + mat[sx - 1][sy] + mat[sx][sy] + mat[sx][sy + 1]
    return max(result1, result2, result3, result4)

def tetromino5(sx, sy):
    result1 = 0; result2 = 0; result3 = 0; result4 = 0
    if 1 <= sx < n and 1 <= sy < m - 1:
        result1 = mat[sx][sy - 1] + mat[sx][sy] + mat[sx][sy + 1] + mat[sx - 1][sy]
    if 1 <= sx < n - 1 and 0 <= sy < m - 1:
        result2 = mat[sx - 1][sy] + mat[sx][sy] + mat[sx + 1][sy] + mat[sx][sy + 1]
    if 0 <= sx < n - 1 and 1 <= sy < m - 1:
        result3 = mat[sx][sy - 1] + mat[sx][sy] + mat[sx][sy + 1] + mat[sx + 1][sy]
    if 1 <= sx < n - 1 and 1 <= sy < m:
        result4 = mat[sx - 1][sy] + mat[sx][sy] + mat[sx + 1][sy] + mat[sx][sy - 1]
    return max(result1, result2, result3, result4)


n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

max_value = 0
for i in range(n):
    for j in range(m):
        tet1 = tetromino1(i, j)
        tet2 = tetromino2(i, j)
        tet3 = tetromino3(i, j)
        tet4 = tetromino4(i, j)
        tet5 = tetromino5(i, j)

        temp = max(tet1, tet2, tet3, tet4, tet5)
        
        if temp > max_value:
            max_value = temp

print(max_value)