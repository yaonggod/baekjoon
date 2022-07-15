k = int(input())
lst = []
for i in range(k):
    lst.append(int(input()))

money = [] 
for i in lst:
    if i != 0:
        money.append(i)
    else:
        money.pop()
   
print(sum(money))
