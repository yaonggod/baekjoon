n = int(input())
a = n
b = 0
c = 0
count = 0
if n == 0:
    count = 1
else:
    while c != n:
        b = a // 10 + a % 10
        c = (a % 10) * 10 + b % 10
        a = c
        count += 1
    
print(count)