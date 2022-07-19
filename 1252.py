n, m = map(str, input().split())

sum_n = 0
for i in range(len(n)):
    if n[-i - 1] == '1':
        sum_n += 2 ** i
        
sum_m = 0
for i in range(len(m)):
    if m[-i - 1] == '1':
        sum_m += 2 ** i
        
sum_total = sum_n + sum_m
print(format(sum_total, 'b'))
    
        