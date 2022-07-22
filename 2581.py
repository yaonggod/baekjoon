m = int(input())
n = int(input())
sosu = []
for i in range(m, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        sosu.append(i)
if sosu == []:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))