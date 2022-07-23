def fibonacci(n):
    lst = [0 for _ in range(n + 1)]
    lst[0] = 0
    lst[1] = 1
    for i in range(2, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]
    return lst[-1]

n = int(input())
print(fibonacci(n))