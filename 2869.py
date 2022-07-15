import math
a, b, v = map(int, input().split())

# (n - 1) * (a - b) + a = v
# n - 1 = (v - a) / (a - b)
n = ((v - a) / (a - b)) + 1
print(math.ceil(n))
