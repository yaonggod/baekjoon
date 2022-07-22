n, k = map(int, input().split())
coin_list = []
for i in range(n):
    coin_list.append(int(input()))
count = 0
for i in range(n - 1, -1, -1):
    if k // coin_list[i] > 0:
        count += k // coin_list[i]
        k = k - (k // coin_list[i]) * coin_list[i]
    else:
        pass
print(count)