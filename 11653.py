n = int(input())
if n == 1:
    pass

sosu = []
for i in range(1, n + 1):
    if n % i == 0:
        sosu.append(i)

while True:      
    for i in range(2, max(sosu) + 1):
        while True:
            if n % i != 0:
                break
            n = n / i
            print(i)
            
    if n == 1:
        break