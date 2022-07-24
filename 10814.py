n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(str, input().split())))

lst.sort(key = lambda humans : int(humans[0]))

for i in range(n):
    print(lst[i][0], lst[i][1])
    
    



        

