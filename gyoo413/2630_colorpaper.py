def merge(mat1, mat2, mat3, mat4):
    l = len(mat1)
    result = [[0] * (2*l) for _ in range(2*l)]

    for i in range(l):
        for j in range(l):
            result[i][j] = mat1[i][j]
            result[l + i][j] = mat3[i][j]
            result[i][l + j] = mat2[i][j]
            result[l + i][l + j] = mat4[i][j]

    return result


def divide(idx, mat):
    if idx == 1:
        return mat
    
    idx //= 2
    first = [arr[:idx] for arr in mat[:idx]]
    second = [arr[idx:] for arr in mat[:idx]]
    third = [arr[:idx] for arr in mat[idx:]]
    fourth = [arr[idx:] for arr in mat[idx:]]

    first_mat = divide(idx, first)
    second_mat = divide(idx, second)
    third_mat = divide(idx, third)
    fourth_mat = divide(idx, fourth)

    return conquer(first_mat, second_mat, third_mat, fourth_mat)

def conquer(mat1, mat2, mat3, mat4):
    global cnt1, cnt0, n
    
    if mat1 == mat2 == mat3 == mat4:
        merge_mat0 = merge(mat1, mat2, mat3, mat4)
        if len(merge_mat0) == n:
            if merge_mat0[0][0] == 1:
                cnt1 += 1
            elif merge_mat0[0][0] == 0:
                cnt0 += 1
        return merge_mat0
    
    if mat1[0][0] == 1:
        cnt1 += 1
    elif mat1[0][0] == 0:
        cnt0 += 1
    if mat2[0][0] == 1:
        cnt1 += 1
    elif mat2[0][0] == 0:
        cnt0 += 1
    if mat3[0][0] == 1:
        cnt1 += 1
    elif mat3[0][0] == 0:
        cnt0 += 1
    if mat4[0][0] == 1:
        cnt1 += 1
    elif mat4[0][0] == 0:
        cnt0 += 1

    merge_mat = merge(mat1, mat2, mat3, mat4)
    for i in range(len(merge_mat)):
        for j in range(len(merge_mat)):
            merge_mat[i][j] = 2

    return merge_mat
    

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
cnt1 = 0; cnt0 = 0

divide(n, matrix)
print(cnt0)
print(cnt1)

