dwarf = []
total = 0
for i in range(9):
    temp = int(input())
    dwarf.append(temp)
    total += temp

for i in range(8):
    for j in range(i + 1, 9):
        hundred = total - dwarf[i] - dwarf[j]
        if hundred == 100:
            out1 = i
            out2 = j

dwarf.pop(out1)
dwarf.pop(out2 - 1)
dwarf.sort()
for i in range(7):
    print(dwarf[i])
