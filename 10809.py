word = input()
word2 = list(map(ord, word))

#알파벳을 0부터 25까지 숫자로 바꾸기
for i in range(len(word2)):
    word2[i] = word2[i] - 97
    
alphabet = [-1 for _ in range(26)]


# word2[0] = 1
# -> alphabet[1] = 0

# word2[1] = 0
# -> alphabet[0] = 1

# word2[2] = 4
# -> alphabet[4] = 2

for i in range(len(word2)):
    if alphabet[word2[i]] != -1:
        continue
    alphabet[word2[i]] = i
    

for i in alphabet:
    print(i, end = " ")