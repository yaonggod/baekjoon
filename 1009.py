n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))   

# 1
# 5
# 6
# 0
# 2 4 8 6 2 4 8 6
# 3 9 7 1 3 9 7 1
# 4 6 4 6 4 6
# 7 9 3 1 7 9 3 1
# 8 4 2 6 8 4 2 6
# 9 1 9 1 9 1

for i in range(n):
    if lst[i][0] % 10 == 1:
        print(1)
    elif lst[i][0] % 10 == 5:
        print(5)
    elif lst[i][0] % 10 == 6:
        print(6)
    elif lst[i][0] % 10 == 0:
        print(10) 
    elif lst[i][0] % 10 == 2:
        if lst[i][1] % 4 == 1:
            print(2)
        elif lst[i][1] % 4 == 2:
            print(4)
        elif lst[i][1] % 4 == 3:
            print(8)
        else:
            print(6)
    elif lst[i][0] % 10 == 3:
        if lst[i][1] % 4 == 1:
            print(3)
        elif lst[i][1] % 4 == 2:
            print(9)
        elif lst[i][1] % 4 == 3:
            print(7)
        else:
            print(1)
    elif lst[i][0] % 10 == 4:
        if lst[i][1] % 2 == 1:
            print(4)
        else:
            print(6)
    elif lst[i][0] % 10 == 7:
        if lst[i][1] % 4 == 1:
            print(7)
        elif lst[i][1] % 4 == 2:
            print(9)
        elif lst[i][1] % 4 == 3:
            print(3)
        else:
            print(1)
    elif lst[i][0] % 10 == 8:
        if lst[i][1] % 4 == 1:
            print(8)
        elif lst[i][1] % 4 == 2:
            print(4)
        elif lst[i][1] % 4 == 3:
            print(2)
        else:
            print(6)
    elif lst[i][0] % 10 == 9:
        if lst[i][1] % 2 == 1:
            print(9)
        else:
            print(1)