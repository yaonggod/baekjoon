n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

min = 0
for i in range(n):
    min += a[i] * b[i]
    
print(min)