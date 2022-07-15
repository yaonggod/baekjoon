word = input()
alphabet = [0 for _ in range(26)]

for i in word:
    i = i.lower()
    alphabet[ord(i) - 97] += 1
    
max_alphabet = max(alphabet)
if alphabet.count(max_alphabet) != 1:
    print("?")
else:
    max_alphabet_index = alphabet.index(max_alphabet)
    print(chr(max_alphabet_index + 97).upper())