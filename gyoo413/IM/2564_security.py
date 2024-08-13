w, h = map(int, input().split())
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
    if lst[-1][0] == 2:
        lst[-1][0] = 3
    elif lst[-1][0] == 3:
        lst[-1][0] = 2
security = list(map(int, input().split()))
if security[0] == 2:
    security[0] = 3
elif security[0] == 3:
    security[0] = 2

def shortest(coord, center):
    x = coord[0]
    y = coord[1]
    center_x = center[0]
    center_y = center[1]

    if center_x == 1:
        if x == 1:
            root = abs(center_y - y)
        elif x == 2:
            root = center_y + y
        elif x == 3:
            root1 = center_y + y + h
            root2 = (w - center_y) + (w - y) + h
            root = min(root1, root2)
        elif x == 4:
            root = (w - center_y) + y

    elif center_x == 2:
        if x == 1:
            root = center_y + y
        elif x == 2:
            root = abs(center_y - y)
        elif x == 3:
            root = (h - center_y) + y
        elif x == 4:
            root1 = center_y + y + w
            root2 = (h - center_y) + (h - y) + w
            root = min(root1, root2)

    elif center_x == 3:
        if x == 1:
            root1 = center_y + y + h
            root2 = (w - center_y) + (w - y) + h
            root = min(root1, root2)
        elif x == 2:
            root = center_y + (h - y)
        elif x == 3:
            root = abs(center_y - y)
        elif x == 4:
            root = (w - center_y) + (h - y)

    elif center_x == 4:
        if x == 1:
            root = center_y + (w - y)
        elif x == 2:
            root1 = center_y + y + w
            root2 = (h - center_y) + (h - y) + w
            root = min(root1, root2)
        elif x == 3:
            root = (h - center_y) + (w - y)
        elif x == 4:
            root = abs(center_y - y)

    return root


ans = 0
for e in lst:
    ans += shortest(e, security)

print(ans)