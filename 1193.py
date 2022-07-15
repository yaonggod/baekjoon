x = int(input())

def sum(n):
    return int(n * (n + 1) / 2)

# (1), (2, 3), (4, 5, 6), (7, 8, 9, 10) ... 으로 구분 가능, 각 그룹의 마지막 항은 sum(n)
# x가 몇 번째 그룹에 속하는지
def x_in(n):
    n = 0
    while sum(n) < x:
        n += 1
    return n

# x가 몇 번째 그룹의 몇 번째 항인지 튜플로 리턴
def x_in_yth(n):
    x_in_range = []
    x_in_minimum = sum((x_in(n)) - 1) + 1
    x_in_maximum = sum((x_in(n)))
    for i in range(x_in_minimum, x_in_maximum + 1):
        x_in_range.append(i)
    x_in_index = x_in_range.index(x)
    return x_in(n), x_in_index + 1

i = x_in_yth(x)[1]   
n = x_in(x)

# 짝수번째 그룹은 내려감    
if n % 2 == 0:
    print(str(i) + "/" + str(n - i + 1))
# 홀수번째 그룹은 올라감
else:
    print(str(n - i + 1) + "/" + str(i))

    
