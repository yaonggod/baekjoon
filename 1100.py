chess = []
for i in range(8):
    chess.append(input())

count = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if chess[i][j] == "F":
                count += 1
            else:
                continue
print(count)
