def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def combination(n, m):
    return factorial(m) / (factorial(n) * factorial(m - n))

t = int(input())
test_case = []
for i in range(t):
    test_case.append(list(map(int, input().split())))
    
for i in test_case:
    print(int(combination(i[0], i[1])))