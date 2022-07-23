def geumminsoo(n : str):
    lst = []
    for i in range(len(n)):
        lst.append(n[i])
    if set(lst) == {'4'} or set(lst) == {'7'} or set(lst) == {'4', '7'}:
        return True
    else:
        return False
n = int(input())
while True:
    if geumminsoo(str(n)) == True:
        break
    n -= 1
print(n)

