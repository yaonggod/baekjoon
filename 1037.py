n = int(input())
lst = list(map(int, input().split()))

new_lst = sorted(lst, reverse=False)
print(new_lst[0] * new_lst[-1])   