n, m = map(int, input().split())
r, c, direction = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

clean = 0
cnt = 0

while True:

    if room[r][c] == 0:
        room[r][c] = 2
        clean += 1

    cleaned = False

    for _ in range(4):

        direction = (direction + 3) % 4
        nr = r + dx[direction]
        nc = c + dy[direction]

        if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
            r, c = nr, nc
            cleaned = True
            break

    if cleaned:
        continue
    
    back_direction = (direction + 2) % 4
    nr = r + dx[back_direction]
    nc = c + dy[back_direction]

    if 0 <= nr < n and 0 <= nc < m and room[nr][nc] != 1:
        r, c = nr, nc
    else:
        break

print(clean)

