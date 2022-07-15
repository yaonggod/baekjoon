x = int(input())

# (1), (2 ~ 7), (8 ~ 19), (20 ~ 37), (38 ~ 61), ...
# 1번째 그룹의 원소 수는 1, n번째 그룹의 원소 수는 6 * (n - 1)

# x가 몇 번째 그룹에 있는지 받기
def x_in(x):
    n = 1
    n_max = 1
    while n_max < x:
        n_max += 6 * n
        n += 1
    return n

print(x_in(x))
    

    




















# # if n == 1:
#     print(1)
# else:
    