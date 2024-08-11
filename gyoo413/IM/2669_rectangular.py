matrix = [list(map(int, input().split())) for _ in range(4)]

area = []
for i in range(4):
    start_x = matrix[i][0]
    start_y = matrix[i][1]

    width = matrix[i][2] - start_x
    height = matrix[i][3] - start_y

    for j in range(1, width + 1):
        for k in range(1, height + 1):
            area.append((start_x + j, start_y + k))

print(len(set(area)))