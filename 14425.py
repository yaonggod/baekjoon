m, n = map(int, input().split())
lst = []
lst2 = []
for i in range(m):
    lst.append(str(input()))
for i in range(n):
    lst2.append(str(input()))
    
count = 0
for i in lst2:
    if i in lst:
        count += 1
        
print(lst, lst2)