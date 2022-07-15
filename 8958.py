T = int(input())
case = []
for i in range(T):
    case.append(input())
    
def score(a : str):
    n = 0
    x = 0
    if a[0] == "O":
        n = 1
        x += n
    else: 
        n = 0
        x += n 
    for i in range(1, len(a)):
        if a[i] == "O":
            n += 1
            x += n
        else:
            n = 0
            x += n
    return x

for i in range(T):
    print(score(case[i]))