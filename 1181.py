n = int(input())
word = []
for i in range(n):
    word.append(input())
    
for i in word:
    if word.count(i) > 1:
        while word.count(i) != 1:
            word.remove(i)
word.sort()
    
word_length_dict = {} 
for i in word:
    word_length_dict[i] = len(i)
    
word_length_list = list(word_length_dict.values())
max_length = max(word_length_list)

for i in range(1, max_length + 1):
    for j in word:
        if len(j) == i:
            print(j)
    