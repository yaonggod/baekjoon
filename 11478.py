s = input()
partial_str = []
for i in range(len(s)):
    for j in range(len(s) - i):
        partial_str.append(s[j:j + i + 1])
print(len(set(partial_str)))