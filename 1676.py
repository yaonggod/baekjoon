import math

n = int(input())
n_fac = str(math.factorial(n))

i = -1
count = 0
while n_fac[i] == '0':
    i -= 1
    count += 1
    
print(count)


