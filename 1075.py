a = int(input())
b = int(input())

a = a - a % 100
while a % b != 0:
    a += 1

c = a % 100
print('%02d' % c)