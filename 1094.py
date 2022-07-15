x = int(input())
lst = [0 for _ in range(7)]
i = 1
while x > 0:
    lst[-i] = x % 2
    x = x // 2
    i += 1
print(sum(lst))
                  