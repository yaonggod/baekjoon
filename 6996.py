n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    if len(a) != len(b):
        print(f'{a} & {b} are NOT anagrams.')
    else:
        dict_a = {}
        dict_b = {}
        for i in range(len(a)):
            if a[i] not in dict_a:
                dict_a[a[i]] = 1
            else:
                dict_a[a[i]] += 1
        for i in range(len(b)):
            if b[i] not in dict_b:
                dict_b[b[i]] = 1
            else:
                dict_b[b[i]] += 1
        if dict_a == dict_b:
            print(f'{a} & {b} are anagrams.')
        else:
            print(f'{a} & {b} are NOT anagrams.')

