n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda xy : (xy[0], xy[1]))

for i in range(n):
    print(lst[i][0], lst[i][1])
    
    



        

