def count_paint(arr, row, col, first_color):
    count = 0
    for i in range(8):
        for j in range(8):
            if (i+j) %2 ==0:
                color = first_color
            else:
                if first_color == 'W':
                    color = 'B'
                else:
                    color ='W'
            if arr[row+i][col+j] != color:
                count +=1

    return count


def find(arr, N, M):
    min_arr = []

    for i in range(N-7):
        for j in range(M-7):
            W = count_paint(arr, i, j, 'W')
            B = count_paint(arr, i, j, 'B')
            min_arr.append(W)
            min_arr.append(B)
            min_value = min(min_arr)

    return min_value




N , M = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]

result = find(arr, N, M)
print(result)


