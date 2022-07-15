import sys
n = int(input())
commands = []
for i in range(n):
    commands.append(list(map(str, sys.stdin.readline().split())))
lst = []
   
def push(x, lst):
    lst.append(x)

def pop(lst):
    if size(lst) == 0:
        return -1
    x = lst[-1]
    del lst[-1]
    return x

def size(lst):
    count = 0
    for i in lst:
        count += 1
    return count

def empty(lst):
    if size(lst) == 0:
        return 1
    else:
        return 0
    
def top(lst):
    if size(lst) == 0:
        return -1
    return lst[-1]

for command in commands:
    if 'push' in command:
        push(int(command[1]), lst)
    elif 'pop' in command:
        print(pop(lst))
    elif 'size' in command:
        print(size(lst))
    elif 'empty' in command:
        print(empty(lst))
    else:
        print(top(lst))