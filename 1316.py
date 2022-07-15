N = int(input())
words = []
for i in range(N):
    words.append(input())

def group(word : str):
    lst = [word[0]]
    a = []
    if len(word) == 1:
        return 1
    else: 
        for i in range(1, len(word)):
            if word[i - 1] != word[i] and word[i] in lst:
                a.append(0)
            else:
                a.append(1)
            lst.append(word[i])
        for i in a:
            if 0 in a:
                return 0
            else:
                return 1

sum_group = []
for i in range(N):
    sum_group.append(group(words[i]))

print(sum(sum_group))

