self_number = []
for i in range(1, 10001):
    self_number.append(i)

# 자릿수 더하는 함수
def digit(n : int):
    sum = 0
    n_str = str(n)
    for i in range(len(n_str)):
        sum += int(n_str[i])
    return sum

for i in range(1, 10001):
    i += digit(i)
    if i in self_number:
        self_number.remove(i)
        
for i in self_number:
    print(i)