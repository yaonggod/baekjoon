n, k = map(int, input().split())
lst = list(map(int, input().split(",")))

for _ in range(k):
    lst_new = [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]
    lst = lst_new
    
for i in range(len(lst) - 1):
    print(lst[i], end = ',')
print(lst[len(lst) - 1])