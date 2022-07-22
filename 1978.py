n = int(input())
lst = list(map(int, input().split()))
sosu = []
for i in lst:
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        sosu.append(i)
print(len(sosu))