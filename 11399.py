n = int(input())
lst = list(map(int, input().split()))
lst.sort()
time_sum = 0
for i in range(n):
    time_sum += lst[i] * (n - i)    
print(time_sum)